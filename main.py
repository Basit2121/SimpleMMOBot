import pyautogui
import keyboard
import random
import time
import threading
import winsound

paused = False
click_speed = 0.8
gathers = input("How Many Times Should I gather In Total : ")

def play_beep(frequency, duration):
    winsound.Beep(frequency, duration)

pyautogui.FAILSAFE = False
pause = False

def pause_resume_function():
    global paused
    while True:
        # Listen for the 'p' key press
        keyboard.wait('p')

        # Toggle the pause state
        paused = not paused

        if paused:
            print("Script paused.")
        else:
            print("Script resumed.")

def hack_loop():

    while keyboard.is_pressed('q') != True:
        
        confirm_existance = None
        
        confirm_existance = pyautogui.locateOnScreen('assets/confirm_existance.png', grayscale=False, confidence=0.9)
        
        if confirm_existance is not None:
            
            print("Confirm Existance and then Press Enter key to Continue.")
            
            play_beep(440, 3000)
            
            input()
            
        else:
            pass
        
        time.sleep(random.uniform(1, 2))
        
        attack = None
        
        attack = pyautogui.locateOnScreen('assets/attack.png', grayscale=False, confidence=0.8)
        
        if attack is not None:
            
            attack_center = pyautogui.center(attack)
            
            attack_offset_x = random.uniform(-100, 100)  
            attack_offset_y = random.uniform(-100, 100) 
            
            attack_x = attack_center.x + attack_offset_x
            attack_y = attack_center.y + attack_offset_y
            
            pyautogui.moveTo(attack_x, attack_y, duration=click_speed)
            
            attack_offset_x = random.uniform(-20, 20)  
            attack_offset_y = random.uniform(-20, 20) 
            
            attack_x = attack_center.x + attack_offset_x
            attack_y = attack_center.y + attack_offset_y
            
            pyautogui.moveTo(attack_x, attack_y, duration=click_speed)
            
            pyautogui.leftClick()
            
            print("Clicking Attack...")
            
            endbattle = None
            
            while endbattle == None:
                
                try:
                    endbattle = pyautogui.locateOnScreen('assets/endbattle.png', grayscale=False, confidence=0.8)
                    
                    endbattle_center = pyautogui.center(endbattle)
                    endbattle_offset_x = random.uniform(-100, 100)  
                    endbattle_offset_y = random.uniform(-100, 100) 
                    
                    endbattle_x = endbattle_center.x + endbattle_offset_x
                    endbattle_y = endbattle_center.y + endbattle_offset_y
                    
                    pyautogui.moveTo(endbattle_x, endbattle_y, duration=click_speed)
                    
                    endbattle_offset_x = random.uniform(-20, 20)  
                    endbattle_offset_y = random.uniform(-20, 20) 
                    
                    endbattle_x = endbattle_center.x + endbattle_offset_x
                    endbattle_y = endbattle_center.y + endbattle_offset_y
                    
                    pyautogui.moveTo(endbattle_x, endbattle_y, duration=click_speed)
            
                    pyautogui.leftClick()
                except:
                    pass
                
                defeated = None
                
                try:
                    defeated = pyautogui.locateOnScreen('assets/defeated.png', grayscale=False, confidence=0.8)
                except:
                    pass
                
                if defeated is not None:
                    
                    print("You Have Been Defeted, Please Restart the Bot.")
            
                    play_beep(440, 3000)
                    
                    input()
                    
                else:
                    pass 
            
                attackbandit = None
                
                attackbandit = pyautogui.locateOnScreen('assets/attackbandit.png', grayscale=False, confidence=0.8)
                
                if attackbandit is not None:
                    
                    attackbandit_center = pyautogui.center(attackbandit)
                    attackbandit_offset_x = random.uniform(-100, 100)  
                    attackbandit_offset_y = random.uniform(-100, 100) 
                    
                    attackbandit_x = attackbandit_center.x + attackbandit_offset_x
                    attackbandit_y = attackbandit_center.y + attackbandit_offset_y
                    
                    pyautogui.moveTo(attackbandit_x, attackbandit_y, duration=click_speed)
                    
                    attackbandit_offset_x = random.uniform(-20, 20)  
                    attackbandit_offset_y = random.uniform(-20, 20) 
                    
                    attackbandit_x = attackbandit_center.x + attackbandit_offset_x
                    attackbandit_y = attackbandit_center.y + attackbandit_offset_y
                    
                    pyautogui.moveTo(attackbandit_x, attackbandit_y, duration=click_speed)
            
                    pyautogui.leftClick()
                    print("Attacking Mob...")
                    
                else:
                    pass
                    
        else:
            print("Attack Not Found...")
            
        time.sleep(random.uniform(0.1, 1.5))
                
        mine = None
        
        mine = pyautogui.locateOnScreen('assets/mine.png', grayscale=False, confidence=0.8)
            
        if mine is not None:
            
            mine_center = pyautogui.center(mine)
            
            mine_offset_x = random.uniform(-100, 100)  
            mine_offset_y = random.uniform(-100, 100) 
            
            mine_x = mine_center.x + mine_offset_x
            mine_y = mine_center.y + mine_offset_y
            
            pyautogui.moveTo(mine, duration=click_speed)
            
            mine_offset_x = random.uniform(-20, 20)  
            mine_offset_y = random.uniform(-20, 20) 
            
            mine_x = mine_center.x + mine_offset_x
            mine_y = mine_center.y + mine_offset_y
            
            pyautogui.moveTo(mine, duration=click_speed)
            
            pyautogui.leftClick()
            
            print("Clicking Mine...")
            
            time.sleep(random.uniform(2, 4))
            
            gather = None
            impossible = None
            gather = pyautogui.locateOnScreen('assets/gather.png', grayscale=False, confidence=0.8)
            impossible = pyautogui.locateOnScreen('assets/impossible.png', grayscale=False, confidence=0.8)
            
            if impossible is not None:
            
                pyautogui.keyDown('alt')
                pyautogui.press('left')
                pyautogui.keyUp('alt')   
            
            elif gather is not None:
                
                for i in range(int(gathers)):
                
                    gather_center = pyautogui.center(gather)
                    gather_offset_x = random.uniform(-100, 100)  
                    gather_offset_y = random.uniform(-100, 100) 
                    gather_x = gather_center.x + gather_offset_x
                    gather_y = gather_center.y + gather_offset_y
                    pyautogui.moveTo(gather_x, gather_y, duration=click_speed)
                    
                    gather_offset_x = random.uniform(-20, 20)  
                    gather_offset_y = random.uniform(-20, 20) 
                    gather_x = gather_center.x + gather_offset_x
                    gather_y = gather_center.y + gather_offset_y
                    pyautogui.moveTo(gather_x, gather_y, duration=click_speed)
                
                    pyautogui.leftClick()
                
                    print("Clicking Gather...")
                    time.sleep(random.uniform(1.5, 3))
                
                time.sleep(random.uniform(2, 4))
                
                close = None
                
                close = pyautogui.locateOnScreen('assets/press_here_to_close.png', grayscale=False, confidence=0.8)
                
                if close is not None:
                
                    close_center = pyautogui.center(close)
                    close_offset_x = random.uniform(-100, 100)  
                    close_offset_y = random.uniform(-100, 100) 
                    close_x = close_center.x + close_offset_x
                    close_y = close_center.y + close_offset_y
                    
                    pyautogui.moveTo(close_x, close_y, duration=click_speed)
                    
                    close_offset_x = random.uniform(-20, 20)  
                    close_offset_y = random.uniform(-20, 20) 
                    close_x = close_center.x + close_offset_x
                    close_y = close_center.y + close_offset_y
                    
                    pyautogui.moveTo(close_x, close_y, duration=click_speed)
            
                    pyautogui.leftClick()
                
                    print("Clicking Close...")
                    
                else:
                    pass       
            else:
                pass
        else:
            print("Mine not found...")
            
        catch = None
        
        catch = pyautogui.locateOnScreen('assets/catch.png', grayscale=False, confidence=0.8)
            
        if catch is not None:
            
            catch_center = pyautogui.center(catch)
            
            catch_offset_x = random.uniform(-100, 100)  
            catch_offset_y = random.uniform(-100, 100) 
            
            catch_x = catch_center.x + catch_offset_x
            catch_y = catch_center.y + catch_offset_y
            
            pyautogui.moveTo(catch, duration=click_speed)
            
            catch_offset_x = random.uniform(-20, 20)  
            catch_offset_y = random.uniform(-20, 20) 
            
            catch_x = catch_center.x + catch_offset_x
            catch_y = catch_center.y + catch_offset_y
            
            pyautogui.moveTo(catch, duration=click_speed)
            
            pyautogui.leftClick()
            
            print("Clicking Catch...")
            
            time.sleep(random.uniform(2, 4))
            
            gather = None
            impossible = None
            gather = pyautogui.locateOnScreen('assets/gather.png', grayscale=False, confidence=0.8)
            impossible = pyautogui.locateOnScreen('assets/impossible.png', grayscale=False, confidence=0.8)
            
            if impossible is not None:
            
                pyautogui.keyDown('alt')
                pyautogui.press('left')
                pyautogui.keyUp('alt')   
            
            elif gather is not None:
                
                for i in range(int(gathers)):
                
                    gather_center = pyautogui.center(gather)
                    gather_offset_x = random.uniform(-100, 100)  
                    gather_offset_y = random.uniform(-100, 100) 
                    gather_x = gather_center.x + gather_offset_x
                    gather_y = gather_center.y + gather_offset_y
                    pyautogui.moveTo(gather_x, gather_y, duration=click_speed)
                    
                    gather_offset_x = random.uniform(-20, 20)  
                    gather_offset_y = random.uniform(-20, 20) 
                    gather_x = gather_center.x + gather_offset_x
                    gather_y = gather_center.y + gather_offset_y
                    pyautogui.moveTo(gather_x, gather_y, duration=click_speed)
                
                    pyautogui.leftClick()
                
                    print("Clicking Gather...")
                    time.sleep(random.uniform(1.5, 3))
                
                time.sleep(random.uniform(2, 4))
                
                close = None
                close = pyautogui.locateOnScreen('assets/press_here_to_close.png', grayscale=False, confidence=0.8)
                
                if close is not None:
                
                    close_center = pyautogui.center(close)
                    close_offset_x = random.uniform(-100, 100)  
                    close_offset_y = random.uniform(-100, 100) 
                    close_x = close_center.x + close_offset_x
                    close_y = close_center.y + close_offset_y
                    
                    pyautogui.moveTo(close_x, close_y, duration=click_speed)
                    
                    close_offset_x = random.uniform(-20, 20)  
                    close_offset_y = random.uniform(-20, 20) 
                    close_x = close_center.x + close_offset_x
                    close_y = close_center.y + close_offset_y
                    
                    pyautogui.moveTo(close_x, close_y, duration=click_speed)
            
                    pyautogui.leftClick()
                
                    print("Clicking Close...")
                else:
                    pass       
            else:
                pass
        else:
            print("Catch not found...")
            
        chop = None
        
        chop = pyautogui.locateOnScreen('assets/chop.png', grayscale=False, confidence=0.8)
            
        if chop is not None:
            
            chop_center = pyautogui.center(chop)
            
            chop_offset_x = random.uniform(-100, 100)  
            chop_offset_y = random.uniform(-100, 100) 
            
            chop_x = chop_center.x + chop_offset_x
            chop_y = chop_center.y + chop_offset_y
            
            pyautogui.moveTo(chop, duration=click_speed)
            
            chop_offset_x = random.uniform(-20, 20)  
            chop_offset_y = random.uniform(-20, 20) 
            
            chop_x = chop_center.x + chop_offset_x
            chop_y = chop_center.y + chop_offset_y
            
            pyautogui.moveTo(chop, duration=click_speed)
            
            pyautogui.leftClick()
            
            print("Clicking Chop...")
            
            time.sleep(random.uniform(2, 4))
            
            gather = None
            impossible = None
            gather = pyautogui.locateOnScreen('assets/gather.png', grayscale=False, confidence=0.8)
            impossible = pyautogui.locateOnScreen('assets/impossible.png', grayscale=False, confidence=0.8)
            
            if impossible is not None:
            
                pyautogui.keyDown('alt')
                pyautogui.press('left')
                pyautogui.keyUp('alt')   
            
            elif gather is not None:
                
                for i in range(int(gathers)):
                
                    gather_center = pyautogui.center(gather)
                    gather_offset_x = random.uniform(-100, 100)  
                    gather_offset_y = random.uniform(-100, 100) 
                    gather_x = gather_center.x + gather_offset_x
                    gather_y = gather_center.y + gather_offset_y
                    pyautogui.moveTo(gather_x, gather_y, duration=click_speed)
                    
                    gather_offset_x = random.uniform(-20, 20)  
                    gather_offset_y = random.uniform(-20, 20) 
                    gather_x = gather_center.x + gather_offset_x
                    gather_y = gather_center.y + gather_offset_y
                    pyautogui.moveTo(gather_x, gather_y, duration=click_speed)
                
                    pyautogui.leftClick()
                
                    print("Clicking Gather...")
                    time.sleep(random.uniform(1.5, 3))
            
                print("Clicking Gather...")
                
                time.sleep(random.uniform(2, 4))
                
                close = None
                close = pyautogui.locateOnScreen('assets/press_here_to_close.png', grayscale=False, confidence=0.8)
                
                if close is not None:
                
                    close_center = pyautogui.center(close)
                    close_offset_x = random.uniform(-100, 100)  
                    close_offset_y = random.uniform(-100, 100) 
                    close_x = close_center.x + close_offset_x
                    close_y = close_center.y + close_offset_y
                    
                    pyautogui.moveTo(close_x, close_y, duration=click_speed)
                    
                    close_offset_x = random.uniform(-20, 20)  
                    close_offset_y = random.uniform(-20, 20) 
                    close_x = close_center.x + close_offset_x
                    close_y = close_center.y + close_offset_y
                    
                    pyautogui.moveTo(close_x, close_y, duration=click_speed)
            
                    pyautogui.leftClick()
                
                    print("Clicking Close...")
                else:
                    pass       
            else:
                pass
        else:
            print("Chop not found...")
            
        salvage = None
        
        salvage = pyautogui.locateOnScreen('assets/salvage.png', grayscale=False, confidence=0.8)
            
        if salvage is not None:
            
            salvage_center = pyautogui.center(salvage)
            
            salvage_offset_x = random.uniform(-100, 100)  
            salvage_offset_y = random.uniform(-100, 100) 
            
            salvage_x = salvage_center.x + salvage_offset_x
            salvage_y = salvage_center.y + salvage_offset_y
            
            pyautogui.moveTo(salvage, duration=click_speed)
            
            salvage_offset_x = random.uniform(-20, 20)  
            salvage_offset_y = random.uniform(-20, 20) 
            
            salvage_x = salvage_center.x + salvage_offset_x
            salvage_y = salvage_center.y + salvage_offset_y
            
            pyautogui.moveTo(salvage, duration=click_speed)
            
            pyautogui.leftClick()
            
            print("Clicking Salvage...")
            
            time.sleep(random.uniform(2, 4))
            
            gather = None
            impossible = None
            gather = pyautogui.locateOnScreen('assets/gather.png', grayscale=False, confidence=0.8)
            impossible = pyautogui.locateOnScreen('assets/impossible.png', grayscale=False, confidence=0.8)
            
            if impossible is not None:
            
                pyautogui.keyDown('alt')
                pyautogui.press('left')
                pyautogui.keyUp('alt')   
            
            elif gather is not None:
                
                for i in range(int(gathers)):
                
                    gather_center = pyautogui.center(gather)
                    gather_offset_x = random.uniform(-100, 100)  
                    gather_offset_y = random.uniform(-100, 100) 
                    gather_x = gather_center.x + gather_offset_x
                    gather_y = gather_center.y + gather_offset_y
                    pyautogui.moveTo(gather_x, gather_y, duration=click_speed)
                    
                    gather_offset_x = random.uniform(-20, 20)  
                    gather_offset_y = random.uniform(-20, 20) 
                    gather_x = gather_center.x + gather_offset_x
                    gather_y = gather_center.y + gather_offset_y
                    pyautogui.moveTo(gather_x, gather_y, duration=click_speed)
                
                    pyautogui.leftClick()
                
                    print("Clicking Gather...")
                    time.sleep(random.uniform(1.5, 3))
            
                print("Clicking Gather...")
                
                time.sleep(random.uniform(2, 4))
                
                close = None
                close = pyautogui.locateOnScreen('assets/press_here_to_close.png', grayscale=False, confidence=0.8)
                
                if close is not None:
                
                    close_center = pyautogui.center(close)
                    close_offset_x = random.uniform(-100, 100)  
                    close_offset_y = random.uniform(-100, 100) 
                    close_x = close_center.x + close_offset_x
                    close_y = close_center.y + close_offset_y
                    
                    pyautogui.moveTo(close_x, close_y, duration=click_speed)
                    
                    close_offset_x = random.uniform(-20, 20)  
                    close_offset_y = random.uniform(-20, 20) 
                    close_x = close_center.x + close_offset_x
                    close_y = close_center.y + close_offset_y
                    
                    pyautogui.moveTo(close_x, close_y, duration=click_speed)
            
                    pyautogui.leftClick()
                
                    print("Clicking Close...")
                else:
                    pass       
            else:
                pass
        else:
            print("Salvage not found...")
        
        time.sleep(random.uniform(0.1, 1.5))
        
        target1 = None
        
        target1 = pyautogui.locateOnScreen('assets/target1.png', grayscale=False, confidence=0.8)
        
        if target1 is not None:
            
            target_center = pyautogui.center(target1)
            
            # Generate random values for x and y offsets
            offset_x = random.uniform(-100, 100)  
            offset_y = random.uniform(-100, 100)  
            
            # Apply the random offsets to the target center
            target_x = target_center.x + offset_x
            target_y = target_center.y + offset_y
            
            # Perform the click at the modified coordinates
            pyautogui.moveTo(target_x, target_y, duration=click_speed)
            
            offset_x = random.uniform(-20, 20)  
            offset_y = random.uniform(-20, 20)  
            
            # Apply the random offsets to the target center
            target_x = target_center.x + offset_x
            target_y = target_center.y + offset_y
            
            # Perform the click at the modified coordinates
            pyautogui.moveTo(target_x, target_y, duration=click_speed)
            
            pyautogui.leftClick()
            
            print("Clicking Step...")
        else:
            print("Step not found...")
        
        time.sleep(random.uniform(0.1, 1.5))
        
        while paused:
            time.sleep(1)
        
main_thread = threading.Thread(target=hack_loop)
pause_thread = threading.Thread(target=pause_resume_function)

main_thread.start()
pause_thread.start()
    