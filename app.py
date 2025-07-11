from camoufox.sync_api import Camoufox
import time
import random
import json
import pyautogui
import os
import google.generativeai as genai
from PIL import Image, ImageTk, ImageDraw, ImageFont
import re
import customtkinter
import tkinterDnD
import warnings
import threading
from browserforge.fingerprints import Screen
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

pyautogui.FAILSAFE = False

def add_text_to_image(image_path, text, position=(10, 10), font_path="arial.ttf", font_size=15, color="black", output_path="output_image.jpg"):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size)
    draw.text(position, text, fill=color, font=font)
    image.save(output_path)

def remove_non_numbers(s):
    return re.sub(r'\D', '', s)

safe = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
    ]

def clear_screen():

    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def remove_non_numbers(text):
    return ''.join(char for char in text if char.isdigit())

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def solve_captcha(page, context):
    screenshot_path = f'div_screenshot_{time.time()}.png'
    output_path = f'image_with_text_{time.time()}.png'
    
    try:
        with context.expect_page() as new_page_info:
            page.click("text=I'm a person! Promise!", timeout=5000)
        new_page = new_page_info.value
        new_page.wait_for_load_state()
        div_text = new_page.inner_text('div.text-2xl.text-gray-800.font-semibold', timeout=5000)
        div = new_page.locator('div.grid.grid-cols-4.gap-2.items-center.justify-center.max-w-sm.mx-auto')
        
        div.screenshot(path=screenshot_path)
        
        add_text_to_image(screenshot_path, f"Which of these resembles {div_text}, give number (numeric)", output_path=output_path)
        
        # Clean up the first screenshot
        try:
            os.remove(screenshot_path)
        except:
            pass
        
        # Change the model to the one you want to use
        genai.configure(api_key='ENTER YOUR API KEY HERE')
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        # Prepare the text prompt
        prompt = f"Look at this image and tell me which numbered option (1-4) best resembles '{div_text}'. Respond only with the number."
        
        # Create a GenerativeContent object with both image and text
        with Image.open(output_path) as img:
            response = model.generate_content(
                [
                    prompt,
                    img
                ]
            )
            
        # Clean up the output image
        try:
            os.remove(output_path)
        except:
            pass
        
        result = int(remove_non_numbers(response.text))
        
        # Click the corresponding button
        buttons = new_page.query_selector_all('.grid.grid-cols-4.gap-2.items-center.justify-center.max-w-sm.mx-auto button')
        if 1 <= result <= len(buttons):
            buttons[result - 1].click()
        else:
            raise ValueError(f"Invalid result number: {result}")
            
        time.sleep(3)
        new_page.close()
        
    except Exception as e:
        print(f"Error in solve_captcha: {str(e)}")
        # Cleanup in case of error
        for file in [screenshot_path, output_path]:
            try:
                if os.path.exists(file):
                    os.remove(file)
            except:
                pass
        raise e
    
def perform_action(page):
    time.sleep(random.uniform(10, 12))
    page.click('text=Gather', timeout=5000)
    time.sleep(random.uniform(10, 12))
    while page.is_visible('text=Press here to gather', timeout=5000):
        page.click('text=Press here to gather')
        time.sleep(random.uniform(10, 12))
    page.click('text=Press here to close', timeout=5000)
    time.sleep(random.uniform(4, 5))

paused = False
pause_condition = threading.Condition()

def pause():
    global paused
    with pause_condition:
        paused = True

def resume():
    global paused
    with pause_condition:
        paused = False
        pause_condition.notify_all()

def check_pause():
    global paused
    with pause_condition:
        while paused:
            pause_condition.wait()
            
def main():

    counts = {
        'steps': 0, 'mine': 0, 'attack': 0, 'salvage': 0, 'chop': 0, 'catch': 0, 'captcha': 0, 'grab':0
    }
    
    while True:
        
        constrains = Screen(max_width=1280, max_height=960)

        with Camoufox(humanize=0.8, screen=constrains) as browser:
            
            context = browser.new_context()

            with open('session.json', 'r') as json_file:
                context.add_cookies(json.load(json_file))

            page = context.new_page()

            page.goto("https://web.simple-mmo.com/travel")
            clear_screen()

            while True:
                check_pause()
                clear_screen()
                
                print(f"CAPTCHA Solved {counts['captcha']} | Steps: {counts['steps']} | Mine: {counts['mine']} | Attack: {counts['attack']} | Salvage: {counts['salvage']} | Chop: {counts['chop']} | Catch: {counts['catch']} | Grab: {counts['grab']}", end='\r', flush=True)

                try:
                    if page.is_visible("text=I'm a person! Promise!", timeout=2000):
                        solve_captcha(page, context)
                        page.click("button:has-text('Take a step')", timeout=20000)
                        counts['captcha'] += 1
                        time.sleep(5)

                    button = page.locator("button:has-text('Take a step')").nth(2)
                    if button.is_visible(timeout=20000):
                        button.click()
                        counts['steps'] += 1
                        
                    time.sleep(2)
                    
                    if checkbox_2.get() == 1:
                        for action in ['Salvage', 'Mine', 'Chop', 'Catch', 'Grab']:
                            if page.is_visible(f'button:has-text("{action}")'):
                                if not page.is_visible('text=Your skill level isn\'t high enough'):
                                    page.click(f'button:has-text("{action}")', timeout=5000)
                                    perform_action(page)
                                    counts[action.lower()] += 1
                            else:
                                pass
                            
                    if checkbox_3.get() == 1:
                        for action in ['Grab']:
                            if page.is_visible(f'button:has-text("{action}")'):
                                if not page.is_visible('text=Your skill level isn\'t high enough'):
                                    page.click(f'button:has-text("{action}")', timeout=5000)
                                    perform_action(page)
                                    counts[action.lower()] += 1
                            else:
                                pass

                    if checkbox_1.get() == 1:
                        if page.is_visible('a:has-text("Attack")'):
                            
                            time.sleep(4)
                            
                            page.click('a:has-text("Attack")', timeout=5000)
                            counts['attack'] = counts['attack'] + 1
                            
                            time.sleep(5)
                            
                            while True:
                                try:
                                    page.click('text=Leave', timeout=5000)
                                    break
                                except:
                                    page.click('text=Attack', timeout=5000)  
                                    time.sleep(random.uniform(3, 4))   

                            time.sleep(random.uniform(4, 5))
                            is_defeat_visible = page.is_visible('text=You have been defeated', timeout=5000)
                            
                            if is_defeat_visible:
                                pyautogui.alert('You have Died, Please heal and Restart the Bot.')
                                input()


                except Exception as e:
                    break

            browser.close()

if __name__ == "__main__":
    
    warnings.filterwarnings("ignore", category=UserWarning)
    customtkinter.set_ctk_parent_class(tkinterDnD.Tk)
    customtkinter.set_appearance_mode("light")
    customtkinter.set_default_color_theme("green")

    app = customtkinter.CTk()
    app.geometry("400x880")
    app.title("SimpleMMO-Bot")

    # Create main scrollable container
    main_container = customtkinter.CTkScrollableFrame(master=app)
    main_container.pack(pady=20, padx=20, fill="both", expand=True)

    # Frame inside scrollable container
    frame_1 = customtkinter.CTkFrame(master=main_container)
    frame_1.pack(pady=20, padx=20, fill="both", expand=True)

    image_path = "logo.png"
    logo_image = Image.open(image_path)
    logo_image = logo_image.resize((300, 300), Image.LANCZOS)
    logo_photo = ImageTk.PhotoImage(logo_image)
    logo_label = customtkinter.CTkLabel(master=frame_1, image=logo_photo, text="")
    logo_label.pack(pady=20)

    label_1 = customtkinter.CTkLabel(
        master=frame_1,
        text="1. Log in to your SimpleMMO Account",
        justify=customtkinter.LEFT,
        font=("Arial", 14)
    )
    label_1.pack(pady=(20, 10), padx=10)

    def save_cookies(output_file: str = "session.json"):
        try:
            constrains = Screen(max_width=1920, max_height=1080)
            with Camoufox(humanize=0.8, screen=constrains) as browser:
                context = browser.new_context()
                page = context.new_page()
                page.goto('https://web.simple-mmo.com/login')
                
                while True:
                    if page.is_visible('text=The start of your journey'):
                        time.sleep(2)
                        break
                cookies = context.cookies()
                with open(output_file, "w") as f:
                    json.dump(cookies, f, indent=2)
                    
                browser.close()
                pyautogui.alert("Login Has Been Saved Successfully, You can Start the bot now")
                return True
        except Exception as e:
            print(f"Error during login: {e}")
            return False

    def login():
        # Disable the button and change text immediately
        login_button.configure(state="disabled", text="Waiting for login to complete...")
        
        # Use after() to run the save_cookies operation in a separate thread
        def perform_login():
            success = save_cookies()
            
            # Use after() to safely update the button from the main thread
            app.after(0, lambda: login_button.configure(
                state="normal",
                text="Login"
            ))
        
        # Start the login process in a separate thread
        thread = threading.Thread(target=perform_login)
        thread.daemon = True  # Make thread daemon so it doesn't prevent app exit
        thread.start()

    login_button = customtkinter.CTkButton(
        master=frame_1,
        text="Login",
        font=("Arial", 12),
        fg_color="blue",
        text_color="white",
        hover_color="darkblue",
        corner_radius=10,
        command=login
    )
    login_button.pack(pady=(0, 20), padx=10)

    label_2 = customtkinter.CTkLabel(
        master=frame_1,
        text="2. Run the Bot and Relax",
        justify=customtkinter.LEFT,
        font=("Arial", 14)
    )
    label_2.pack(pady=(20, 10), padx=10)

    checkbox_1 = customtkinter.CTkCheckBox(master=frame_1, text="Attack Mobs/NPCs")
    checkbox_1.pack(pady=10, padx=10)

    checkbox_2 = customtkinter.CTkCheckBox(master=frame_1, text="Gather Loot")
    checkbox_2.pack(pady=10, padx=10)
    
    checkbox_3 = customtkinter.CTkCheckBox(master=frame_1, text="Grab Event Loot")
    checkbox_3.pack(pady=10, padx=10)

    message = customtkinter.CTkLabel(
        master=frame_1,
        text="(keeping the Gather and Attack disabled will make \nthe stepping alot faster)",
        font=("Arial", 11),
        text_color="grey"
    )
    message.pack(pady=10)

    def change_button_2_text(new_text):
        button_2.configure(text=new_text)

    def run_main():
        app.after(0, change_button_2_text, "Running")
        thread = threading.Thread(target=main)
        thread.start()

    button_2 = customtkinter.CTkButton(
        master=frame_1,
        text="Start",
        font=("Arial", 12),
        fg_color="green",
        text_color="white",
        hover_color="darkgreen",
        corner_radius=10,
        command=run_main
    )
    button_2.pack(pady=(10, 20), padx=10)
    
    def change_button_text(button, new_text):
        button.configure(text=new_text)
    
    def toggle_pause():
        global paused
        if paused:
            resume()
            change_button_text(pause_button, "Pause")
        else:
            pause()
            change_button_text(pause_button, "Resume")
    
    pause_button = customtkinter.CTkButton(
        master=frame_1,
        text="Pause",
        font=("Arial", 12),
        fg_color="orange",
        text_color="white",
        hover_color="darkorange",
        corner_radius=10,
        command=toggle_pause
    )
    pause_button.pack(pady=(0, 20), padx=10)

    footer_label = customtkinter.CTkLabel(
        master=frame_1,
        text="Github: https://github.com/Basit2121/SimpleMMOBot",
        font=("Arial", 11),
        text_color="grey"
    )
    footer_label.pack(pady=10)

    app.mainloop()