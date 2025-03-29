import sys
sys.path.append('/home/nebula/.local/lib/python3.10/site-packages')
import os
import difflib
import threading
import queue
import keyboard
import time
import tempfile

import nltk
from nltk.tokenize import sent_tokenize
# nltk.download('punkt')
# Download NLTK data (punkt for sentence tokenization)

# Set the download path to your home directory
# nltk.download('punkt', download_dir=os.path.expanduser('~/nltk_data'))
# nltk.data.path.append(os.path.expanduser('~/nltk_data'))
# nltk.download('punkt', quiet=True)
try:
    import nltk
    nltk.data.path.append('/home/nebula/nltk_data')  # Your user-specific path
    from nltk.tokenize import sent_tokenize
    
    # Verify punkt is available
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        print("Downloading punkt tokenizer...")
        nltk.download('punkt', download_dir='/home/nebula/nltk_data')
        
except ImportError:
    # Fallback if NLTK not available
    def sent_tokenize(text):
        return [s.strip() for s in text.split('.') if s.strip()]
# Try multiple PDF libraries
try:
    import pdfplumber
    PDF_LIBRARY = 'pdfplumber'
except ImportError:
    try:
        import PyPDF2
        PDF_LIBRARY = 'PyPDF2'
    except ImportError:
        try:
            import pikepdf
            PDF_LIBRARY = 'pikepdf'
        except ImportError:
            PDF_LIBRARY = None

# Text-to-Speech libraries
try:
    from gtts import gTTS
    from pydub import AudioSegment
    from pydub.playback import play
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False

class NaturalVoiceReader:
    def __init__(self, pdf_path, start_page=0, language='en'):
        """
        Initialize the Natural Voice PDF Reader
        
        Parameters:
        pdf_path (str): Path to the PDF file
        start_page (int): Page number to start reading from (0-indexed)
        language (str): Language code for speech synthesis
        """
        if not TTS_AVAILABLE:
            raise ImportError("Required text-to-speech libraries not installed. "
                              "Please install gtts and pydub.")
        
        if not PDF_LIBRARY:
            raise ImportError("No PDF reading library found. "
                              "Please install pdfplumber, PyPDF2, or pikepdf.")
        
        self.pdf_path = pdf_path
        self.start_page = start_page
        self.language = language
        
        # Control flags
        self.is_paused = False
        self.is_running = True
        
        # Queue for communication between threads
        self.text_queue = queue.Queue()
        
        # Temporary directory for audio files
        self.temp_dir = tempfile.mkdtemp()
        
        # Keyboard interrupt handling
        self.setup_keyboard_listeners()
    
    def setup_keyboard_listeners(self):
        """
        Set up keyboard listeners for pause, resume, and exit
        """
        # Pause/Resume listener
        keyboard.add_hotkey('space', self.toggle_pause)
        
        # Exit listener
        keyboard.add_hotkey('esc', self.force_exit)
    
    def text_to_speech(self, text):
        """
        Enhanced version with NLTK sentence segmentation
        """
        temp_audio = os.path.join(self.temp_dir, f'speech_{hash(text)}.mp3')
        
        try:
            # Clean text
            clean_text = ' '.join(text.split())
            
            # Handle common abbreviations before tokenization
            abbreviation_map ={
    # Academic Degrees
    'Ph.D.': 'Doctor of Philosophy',
    'M.D.': 'Medical Doctor',
    'D.D.S.': 'Doctor of Dental Surgery',
    'D.V.M.': 'Doctor of Veterinary Medicine',
    'J.D.': 'Juris Doctor',
    'M.B.A.': 'Master of Business Administration',
    'M.Sc.': 'Master of Science',
    'B.A.': 'Bachelor of Arts',
    'B.Sc.': 'Bachelor of Science',
    
    # Professional Titles
    'Dr.': 'Doctor',
    'Prof.': 'Professor',
    'Rev.': 'Reverend',
    'Hon.': 'Honorable',
    'Sr.': 'Senior',
    'Jr.': 'Junior',
    'Esq.': 'Esquire',
    
    # Personal Titles
    'Mr.': 'Mister',
    'Mrs.': 'Missus',
    'Ms.': 'Mizz',
    'Miss': 'Miss',
    'Mx.': 'Mix',
    
    # Military Ranks
    'Gen.': 'General',
    'Col.': 'Colonel',
    'Maj.': 'Major',
    'Capt.': 'Captain',
    'Lt.': 'Lieutenant',
    'Sgt.': 'Sergeant',
    'Cpl.': 'Corporal',
    'Pvt.': 'Private',
    # Additional common ones
    'Dept.': 'Department',
    'Univ.': 'University',
    'Assn.': 'Association',
    'Bldg.': 'Building',
    'Ave.': 'Avenue',
    'Blvd.': 'Boulevard',
    'St.': 'Street',
    'Rd.': 'Road',
    'Ln.': 'Lane',
    'Pkwy.': 'Parkway',
    'Ste.': 'Suite',
    'Rm.': 'Room',
    'No.': 'Number',
    'attn.': 'attention',
    'c/o': 'care of',
    'ASAP': 'as soon as possible',
    'RSVP': 'please respond',
    'FAQ': 'frequently asked questions',
    'ETA': 'estimated time of arrival',
    'DIY': 'do it yourself',
    'TBA': 'to be announced',
    'TBD': 'to be determined',
    'FYI': 'for your information',
    'AKA': 'also known as',
    'POV': 'point of view',
    'IQ': 'intelligence quotient',
    'EQ': 'emotional quotient',
    'e.g.': 'for example',
    'i.e.': 'that is',
    'etc.': 'and so on',
    'et al.': 'and others',
    'viz.': 'namely',
    'cf.': 'compare',
    'c.': 'circa',
    'vs.': 'versus',
    'v.': 'versus',
    'N.B.': 'note well',
    'P.S.': 'postscript',
    'approx.': 'approximately',
    'no.': 'number',
    'p.': 'page',
    'pp.': 'pages',
    'vol.': 'volume',
    'ed.': 'edition',
    'fig.': 'figure',
    'para.': 'paragraph',
    'sec.': 'section',
    'ref.': 'reference',
    'ex.': 'example',
    'max.': 'maximum',
    'min.': 'minimum',
    'temp.': 'temperature',
    'cal.': 'calories',
    'alt.': 'altitude',
    'lat.': 'latitude',
    'long.': 'longitude',
     'a.m.': 'ante meridiem',
    'p.m.': 'post meridiem',
    'Jan.': 'January',
    'Feb.': 'February',
    'Mar.': 'March',
    'Apr.': 'April',
    'Jun.': 'June',
    'Jul.': 'July',
    'Aug.': 'August',
    'Sep.': 'September',
    'Sept.': 'September',
    'Oct.': 'October',
    'Nov.': 'November',
    'Dec.': 'December',
    'Mon.': 'Monday',
    'Tue.': 'Tuesday',
    'Tues.': 'Tuesday',
    'Wed.': 'Wednesday',
    'Thu.': 'Thursday',
    'Thur.': 'Thursday',
    'Thurs.': 'Thursday',
    'Fri.': 'Friday',
    'Sat.': 'Saturday',
    'Sun.': 'Sunday',
    'in.': 'inches',
    'ft.': 'feet',
    'yd.': 'yards',
    'mi.': 'miles',
    'km.': 'kilometers',
    'm.': 'meters',
    'cm.': 'centimeters',
    'mm.': 'millimeters',
    'lb.': 'pounds',
    'oz.': 'ounces',
    'gal.': 'gallons',
    'pt.': 'pints',
    'qt.': 'quarts',
    'L.': 'liters',
    'mL.': 'milliliters',
    'kph.': 'kilometers per hour',
    'mph.': 'miles per hour',
     'Co.': 'Company',
    'Corp.': 'Corporation',
    'Inc.': 'Incorporated',
    'Ltd.': 'Limited',
    'LLC': 'Limited Liability Company',
    'LP': 'Limited Partnership',
    'CEO': 'Chief Executive Officer',
    'CFO': 'Chief Financial Officer',
    'CTO': 'Chief Technology Officer',
    'VP': 'Vice President',
    'HR': 'Human Resources',
    'R&D': 'Research and Development',
    'PR': 'Public Relations',}
            
            for abbr, expansion in abbreviation_map.items():
                clean_text = clean_text.replace(abbr, expansion)
            
            # Use NLTK for proper sentence segmentation
            sentences = sent_tokenize(clean_text)
            
            # Process each sentence with natural pauses
            full_audio = AudioSegment.silent(duration=100)
            for sentence in sentences:
                if not sentence.strip():
                    continue
                    
                tts = gTTS(
                    text=sentence,
                    lang=self.language,
                    slow=False,
                    lang_check=False
                )
                tts.save(temp_audio)
                
                if os.path.exists(temp_audio):
                    segment = AudioSegment.from_mp3(temp_audio)
                    full_audio += segment
                    full_audio += AudioSegment.silent(duration=150)  # Pause between sentences
                    os.remove(temp_audio)
            
            # Save combined audio
            full_audio.export(temp_audio, format="mp3")
            return temp_audio
            
        except Exception as e:
            print(f"Error generating speech: {e}")
            return None

    def toggle_pause(self):
        """
        Toggle pause/resume of audio playback
        """
        self.is_paused = not self.is_paused
        if self.is_paused:
            print("\n[PAUSED] Press SPACE to resume, ESC to exit")
        else:
            print("\n[RESUMED] Continuing reading")
    
    def force_exit(self):
        """
        Force exit the audio reader
        """
        print("\n[EXITING] Stopping audio playback")
        self.is_running = False
    
    def audio_player_thread(self):
        """
        Thread for playing audio from the queue
        """
        while self.is_running:
            try:
                # Wait for audio file with a timeout
                audio_file = self.text_queue.get(timeout=1)
                
                # Wait if paused
                while self.is_paused:
                    time.sleep(0.1)
                    if not self.is_running:
                        return
                
                # Play the audio
                if audio_file and os.path.exists(audio_file):
                    audio = AudioSegment.from_mp3(audio_file)
                    play(audio)
                    
                    # Clean up temporary audio file
                    os.remove(audio_file)
            
            except queue.Empty:
                # No audio in queue, just continue
                continue
            except Exception as e:
                print(f"Error in audio player: {e}")
                break
    
    def read_pdf(self):
        """
        Read PDF document aloud using the available PDF library
        """
        try:
            # Select PDF reading method based on available library
            if PDF_LIBRARY == 'pdfplumber':
                import pdfplumber
                with pdfplumber.open(self.pdf_path) as pdf:
                    return self._read_pdf_pages(pdf.pages)
            
            elif PDF_LIBRARY == 'PyPDF2':
                import PyPDF2
                with open(self.pdf_path, 'rb') as file:
                    pdf_reader = PyPDF2.PdfReader(file)
                    return self._read_pdf_pages(pdf_reader.pages)
            
            elif PDF_LIBRARY == 'pikepdf':
                import pikepdf
                pdf = pikepdf.Pdf.open(self.pdf_path)
                return self._read_pdf_pages(pdf.pages)
            
            else:
                raise ImportError("No PDF library available")
        
        except Exception as e:
            print(f"Error reading PDF: {e}")
            return False
    
    def _read_pdf_pages(self, pages):
        """
        Common method to read PDF pages
        
        Parameters:
        pages (list): List of PDF pages from different libraries
        
        Returns:
        bool: Success status
        """
        try:
            # Validate page range
            total_pages = len(pages)
            if self.start_page < 0 or self.start_page >= total_pages:
                print(f"Invalid start page. Please choose a page between 0 and {total_pages - 1}")
                return False
            
            # Print book details
            print(f"Reading '{self.pdf_path}' starting from page {self.start_page + 1}")
            print("Controls:")
            print("- SPACE: Pause/Resume")
            print("- ESC: Exit")
            
            # Start audio player thread
            player_thread = threading.Thread(target=self.audio_player_thread)
            player_thread.start()
            
            # Read pages from start_page to end
            for page_num in range(self.start_page, total_pages):
                # Check if should continue
                if not self.is_running:
                    break
                
                # Extract text from the page
                try:
                    if PDF_LIBRARY == 'pdfplumber':
                        text = pages[page_num].extract_text()
                    elif PDF_LIBRARY == 'PyPDF2':
                        text = pages[page_num].extract_text()
                    elif PDF_LIBRARY == 'pikepdf':
                        text = pages[page_num].get_text()
                    else:
                        text = ""
                except Exception as e:
                    print(f"Error extracting text from page {page_num}: {e}")
                    text = ""
                
                # Print page number for reference
                print(f"Reading Page {page_num + 1}")
                
                # Convert text to speech and add to queue
                if text and text.strip():
                    audio_file = self.text_to_speech(text)
                    if audio_file:
                        self.text_queue.put(audio_file)
            
            # Wait for audio player thread to finish
            player_thread.join()
            
            print("Finished reading PDF.")
            return True
        
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
        finally:
            # Remove keyboard listeners
            keyboard.unhook_all()
            
            # Clean up temporary directory
            import shutil
            shutil.rmtree(self.temp_dir, ignore_errors=True)

def find_pdf_in_directory(book_name):
    """
    Search for PDF files in the current directory that match the given book name.
    
    Parameters:
    book_name (str): Name of the book to search for
    
    Returns:
    str: Path to the most likely PDF file, or None if no match found
    """
    # Get all PDF files in the current directory
    pdf_files = [f for f in os.listdir('.') if f.lower().endswith('.pdf')]
    
    if not pdf_files:
        print("No PDF files found in the current directory.")
        return None
    
    # If only one PDF exists, return it
    if len(pdf_files) == 1:
        return pdf_files[0]
    
    # Find the best match using difflib
    matches = difflib.get_close_matches(book_name.lower(), 
                                         [f.lower() for f in pdf_files], 
                                         n=1, 
                                         cutoff=0.3)
    
    if matches:
        # Find the original filename that matches
        matched_file = [f for f in pdf_files if f.lower() == matches[0]][0]
        return matched_file
    
    # If no close match, show available PDFs
    print("Available PDF files:")
    for pdf in pdf_files:
        print(f"- {pdf}")
    
    return None

def main():
    """
    Main function to run the PDF Audio Reader
    """
    # Print available PDF libraries
    print(f"Using PDF library: {PDF_LIBRARY}")
    
    # Prompt user for book name
    book_name = input("Enter the name of the book to read: ")
    
    # Find the PDF file
    pdf_path = find_pdf_in_directory(book_name)
    
    if not pdf_path:
        print(f"Could not find a PDF for '{book_name}'")
        return
    
    # Optional: Specify start page
    start_page_input = input("Enter the page to start reading from (default is 0): ")
    start_page = int(start_page_input) if start_page_input.strip() else 0
    
    # Create and run the PDF Audio Reader
    reader = NaturalVoiceReader(pdf_path, start_page)
    reader.read_pdf()

# Run the main function
if __name__ == "__main__":
    main()