print("[Loading Library and Environment...]")
import ai, ai2
import env
import time, os, re
import pickle
import pyautogui
import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

email = env.EMAIL
password = env.PASSWORD
if email == "" and password == "":
    print("[ File .env is Empty ]")
    exit()
print(f"[ Email: {email} | Password: {password} ]")

LinkLogin = (
    "https://www.coursera.org/login"
)

def stop_execution():
    print("\nKombinasi tombol terdeteksi. Menghentikan loop...")
    global stop_loop
    stop_loop = True
    
first = True
target_nilai = 100
modequiz = False

while True:
    nilai = []
    inputLink = input("\nInput link course (Banyak link pisahkan dengan spasi): ")
    Link = inputLink.split()
    print(f"\nJumlah Course yng di Input: {len(Link)}")

    print("[Memuat Browser...]")
    profile_path = r"C:\Users\runneradmin\AppData\Roaming\Mozilla\Firefox\Profiles\406qyncq.default-release"
    firefox_options = Options()
    firefox_options.set_preference("profile", profile_path)
    firefox_options.add_argument("--disable-popup-blocking")
    firefox_options.set_preference("browser.link.open_newwindow", 1)
    firefox_options.set_preference("browser.link.open_newwindow.restriction", 0)
    driver = webdriver.Firefox(options=firefox_options)

    def login():
        print("[Memuat login...]")
        driver.get(LinkLogin)
        try:
            cookies = pickle.load(open("cookies.pkl", "rb"))
            for cookie in cookies:
                # Tambahkan atribut 'secure' jika SameSite=None
                if cookie.get('sameSite') == 'None' and not cookie.get('secure'):
                    cookie['secure'] = True
                try:
                    driver.add_cookie(cookie)
                except Exception as e:
                    print(f"Gagal menambahkan cookie: {cookie.get('name')} - {e}")
        except:
            print("[SILAKAN LOGIN TERLEBIH DAHULU]")

            indikasi = input("Sudah login [y/n]? ")
            
            if indikasi == "n":
                print("[EXIT]")
            else:
                print("[Menyimpan Cookie...]")
                pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
                time.sleep(1)
                print("[Memuat ulang webdriver...]")
        
        driver.refresh()
        
        
    
    if first:
        login()
        first = False
        
    for index, course in enumerate(Link):
        stop_loop = False
        driver.get(course)
        print("[Memuat Cookie...]")
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            # Tambahkan atribut 'secure' jika SameSite=None
            if cookie.get('sameSite') == 'None' and not cookie.get('secure'):
                cookie['secure'] = True
            try:
                driver.add_cookie(cookie)
            except Exception as e:
                print(f"Gagal menambahkan cookie: {cookie.get('name')} - {e}")

        driver.refresh()
        
        try:
            while not stop_loop:
                try:
                    WebDriverWait(driver, 2).until(
                        EC.visibility_of_element_located((By.CLASS_NAME, "css-y3t86r"))
                    )
                    ul_element = driver.find_element(By.CLASS_NAME, "css-y3t86r")
                    if ul_element:
                        list_items = ul_element.find_elements(By.TAG_NAME, "li")
                        print(f"Jumlah Module di Course {index+1}: {len(list_items)}")
                        break
                except:
                    break
            
            work_ai_1 = 1
            work_ai_2 = 1 
            
            print(f"Eksekusi Course [{course}]")
            while not stop_loop:
                try:
                    WebDriverWait(driver, 3).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, ".css-ra3hwj"))
                    )
                    driver.find_element(By.CSS_SELECTOR, ".css-ra3hwj").click()
                except:
                    pyautogui.click(500, 500)
                    
                # --------------------------
                yngsalah = []
                jawabane = []
                againlagi = True
                htungkuis = 0
                while True:
                    try:
                        popup = driver.find_element(
                            By.XPATH, "//span[@class='cds-button-label' and text()='Close']"
                        )
                        if popup:
                            popup.click()
                    except:
                        pass
                    try:
                        popup = driver.find_element(By.XPATH, "//span[@class='cds-button-label' and text()='Continue']")
                        if popup:
                            popup.click()
                    except:
                        pass
                    try:
                        popupAwal = driver.find_element(By.CSS_SELECTOR, ".c-modal-x-out")
                        if popupAwal:
                            popupAwal.click()
                    except:
                        pass
                    
                    try:
                        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//div[@contenteditable="true"]')))
                        TextArea = driver.find_element(By.XPATH, '//div[@contenteditable="true"]')
                        if TextArea:
                            TextArea.send_keys("p")
                            time.sleep(2)
                            try:
                                WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//button[text()="Reply"]')))
                                driver.find_element(By.XPATH, '//button[text()="Reply"]').click()
                            except:
                                pass
                            try: 
                                WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@id, 'thread_reply_button')]"))).click()
                            except:
                                pass
                            print("[DISCUSSION PROMPT HAS BEEN SENDED]")
                            WebDriverWait(driver, 3).until(
                                EC.visibility_of_element_located(
                                    (By.XPATH, "//button[@aria-label='Next Item']")
                                )
                            )
                            driver.find_element(
                                By.XPATH, "//button[@aria-label='Next Item']"
                            ).click()
                            print("[Next]")
                            continue
                    except:
                        pass
                                        
                    try:
                        WebDriverWait(driver, 3).until(
                            EC.visibility_of_element_located((By.TAG_NAME, "video"))
                        )
                        video = driver.find_element(By.TAG_NAME, "video")
                        if video:
                            pyautogui.click(1000, 480)
                            time.sleep(2)
                            pyautogui.click(1800, 750)
                            time.sleep(1)
                            pyautogui.click(1800, 750)
                            time.sleep(1.5)
                            pyautogui.click(1000, 480)
                            time.sleep(1.5)
                            print("[Video Mark as Done]")
                            WebDriverWait(driver, 3).until(
                                EC.visibility_of_element_located(
                                    (By.XPATH, "//button[@aria-label='Go to next item']")
                                )
                            )
                            driver.find_element(
                                By.XPATH, "//button[@aria-label='Go to next item']"
                            ).click()
                            print("[Next]")
                            continue
                    except Exception as e:
                        pass
                    try:
                        WebDriverWait(driver, 2).until(
                            EC.visibility_of_element_located(
                                (
                                    By.XPATH,
                                    "//span[@class='cds-button-label' and text()='Mark as completed']",
                                )
                            )
                        )
                        mark = driver.find_element(
                            By.XPATH,
                            "//span[@class='cds-button-label' and text()='Mark as completed']",
                        )
                        if mark:
                            mark.click()
                            print("[Reading Mark as Done]")
                            WebDriverWait(driver, 3).until(
                                EC.visibility_of_element_located(
                                    (By.XPATH, "//button[@aria-label='Go to next item']")
                                )
                            )
                            driver.find_element(
                                By.XPATH, "//button[@aria-label='Go to next item']"
                            ).click()
                            print("[Next]")
                            continue
                    except Exception as e:
                        pass

                    try:
                        WebDriverWait(driver, 3).until(
                            EC.visibility_of_element_located(
                                (By.XPATH, "//button[@aria-label='Go to next item']")
                            )
                        )
                        driver.find_element(
                            By.XPATH, "//button[@aria-label='Go to next item']"
                        ).click()
                        print("[Next]")
                    except Exception as e:
                        try:
                            popupAwal = driver.find_element(
                                By.CSS_SELECTOR, ".c-modal-x-out"
                            )
                            if popupAwal:
                                popupAwal.click()
                        except:
                            pass
                        try:
                            popup = driver.find_element(
                                By.XPATH,
                                "//span[@class='cds-button-label' and text()='Close']",
                            )
                            if popup:
                                popup.click()
                        except:
                            break

                    try:
                        popup = driver.find_element(
                            By.XPATH, "//span[@class='cds-button-label' and text()='Close']"
                        )
                        if popup:
                            popup.click()
                    except:
                        pass
                break
        except KeyboardInterrupt:
            print("[Proses dihentikan oleh pengguna]")
            continue
        
    print("COURSE SUDAH SELESAI DI BOT")
    again = input("Mau Input Course Lgi [y/n]? ")
    if again == "n" or again == "N":
        break
    print("\n")
