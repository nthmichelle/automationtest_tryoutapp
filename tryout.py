import unittest
import time
import random
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    udid='emulator-5554',
    appPackage='com.salugan.cobakeluar',
    appActivity='com.salugan.cobakeluar.ui.activity.main.MainActivity',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, capabilities)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def scroll(self, times = 1, multiplier = 1) -> None:
        x = self.driver.get_window_rect()['width']
        y = self.driver.get_window_rect()['height']

        for i in range(times):
            self.driver.swipe(x/2, multiplier*3*y/4, x/2, multiplier*1.5*y/4)

    def check_element_presence(self, element_id) -> bool:
        try:
            self.driver.find_element(by=AppiumBy.ID, value=element_id)
            return True 
        except:
            return False 
        
    def test_01_regis(self) -> None:
        self.driver.implicitly_wait(10)
        print("\nQuestion Review Test\n=======================================")
        
        google_btn = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/btnLoginGoogle')
        google_btn.click()
        time.sleep(3)

        choose_acc = self.driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]')
        choose_acc.click()
        time.sleep(3)

        try:
            login_success = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/iconProfile')
            if(login_success.is_displayed()):
                print("Pengguna telah berhasil login")
        except:
            self.driver.implicitly_wait(5)
            print("Anda belum login, silakan login terlebih dahulu")
        time.sleep(5)
        

        numerasi_btn = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/button')
        numerasi_btn.click()
        time.sleep(3)

        mulai_btn = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/btnGeometriPengukuran')
        mulai_btn.click()
        time.sleep(10)

        soal6 = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.LinearLayout[@content-desc="6"]/android.widget.TextView')
        soal6.click()
        time.sleep(3)

        jawab_soal = self.driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]')
        jawab_soal.click()
        time.sleep(3)

        jawab_btn = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/btnJawab')
        jawab_btn.click()
        time.sleep(2)

        try:
            pembahasan = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/bottom_sheet')
            if(pembahasan.is_displayed()):
                print("Pembahasan soal ditampilkan")
                time.sleep(5)
                self.scroll(2)
        except:
            self.driver.implicitly_wait(5)
            print("Pembahasan tidak tampil")
        time.sleep(5)
    
    
    def test_02_button_tryout(self) -> None:
        self.driver.implicitly_wait(10)
        print("\nTryout Questions Test\n=======================================")
        
        google_btn = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/btnLoginGoogle')
        google_btn.click()
        time.sleep(3)

        choose_acc = self.driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]')
        choose_acc.click()
        time.sleep(3)

        try:
            login_success = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/iconProfile')
            if(login_success.is_displayed()):
                print("Pengguna telah berhasil login")
        except:
            self.driver.implicitly_wait(5)
            print("Anda belum login, silakan login terlebih dahulu")
        time.sleep(5)
        

        numerasi_btn = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/button')
        numerasi_btn.click()
        time.sleep(3)

        mulai_btn = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/btnGeometriPengukuran')
        mulai_btn.click()
        time.sleep(5)

        for i in range(3):
            try:
                button_group = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/linearLayout3')
                if(button_group.is_displayed()):
                    print("Button previous, jawab, dan next ditemukan")
                    next_btn = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/btnNext')
                    next_btn.click()
            except:
                self.driver.implicitly_wait(2)
                print("Pengguna harus scroll terlebih dahulu untuk menemukan button")
                self.scroll(2)
                button_group = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/linearLayout3')
                if(button_group.is_displayed()):
                    print("Button previous, jawab, dan next akhirnya ditemukan")
            time.sleep(5)


    def test_07_histori(self) -> None:
        self.driver.implicitly_wait(10)
        print("\nDownload Report Test\n=======================================")
        
        google_btn = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/btnLoginGoogle')
        google_btn.click()
        time.sleep(3)

        choose_acc = self.driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]')
        choose_acc.click()
        time.sleep(3)

        try:
            login_success = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/iconProfile')
            if(login_success.is_displayed()):
                print("Pengguna telah berhasil login")
        except:
            self.driver.implicitly_wait(5)
            print("Anda belum login, silakan login terlebih dahulu")
        time.sleep(5)
        

        numerasi_btn = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/button')
        numerasi_btn.click()
        time.sleep(3)

        histori_btn = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/btnHistory')
        histori_btn.click()
        time.sleep(2)

        try:
            list_histori = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/recycleView')
            if(list_histori.is_displayed()):
                print("Satu atau lebih histori ditemukan, anda bisa mendownloadnya")
        except:
            self.driver.implicitly_wait(5)
            print("Anda belum memiliki histori apapun")
        time.sleep(3)

        download_btn = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/btnCetak')
        download_btn.click()
        time.sleep(2)

        # Switch to another app
        print("Silakan cek galeri anda")
        self.driver.start_activity('com.google.android.apps.photos', 'com.google.android.apps.photos.home.HomeActivity')
        time.sleep(2)

        notnow_btn = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.apps.photos:id/negative_button')
        notnow_btn.click()
        time.sleep(2)

        library_menu = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.apps.photos:id/tab_library')
        library_menu.click()
        time.sleep(2)

        lihat_foto = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.apps.photos:id/album_cover_view')
        lihat_foto.click()
        time.sleep(2)

        choose_photo = self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@content-desc="Photo taken on Sep 18, 2023 4:52:51 PM"]')
        choose_photo.click()
        time.sleep(2)


    def test_03_multiplechoice(self) -> None:
        self.driver.implicitly_wait(10)
        print("\nMultiple-Choice Questions Test\n=======================================")
        
        google_btn = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/btnLoginGoogle')
        google_btn.click()
        time.sleep(3)

        choose_acc = self.driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]')
        choose_acc.click()
        time.sleep(3)

        try:
            login_success = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/iconProfile')
            if(login_success.is_displayed()):
                print("Pengguna telah berhasil login")
        except:
            self.driver.implicitly_wait(5)
            print("Anda belum login, silakan login terlebih dahulu")
        time.sleep(5)
        

        numerasi_btn = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/button')
        numerasi_btn.click()
        time.sleep(3)

        mulai_btn = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/btnDataDanKetidakpastian')
        mulai_btn.click()
        time.sleep(5)

        
        actions = ActionChains(self.driver)
        #actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(959, 439)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(63, 422)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

        
        soal8 = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.LinearLayout[@content-desc="8"]/android.widget.TextView')
        soal8.click()
        time.sleep(3)
        self.scroll(2)

        print("Anda belum memilih jawaban apapun")
        jawab_btn = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/btnJawab')
        jawab_btn.click()
        try:
            pembahasan = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/bottom_sheet')
            if(pembahasan.is_displayed()):
                print("Pembahasan langsung ditampilkan tanpa alert")
        except:
            print("Pilih jawaban terlebih dahulu")
        time.sleep(3)


    def test_04_submitconfirm(self) -> None:
        self.driver.implicitly_wait(10)
        print("\nConfirmation to Submit Answers\n=======================================")
        
        google_btn = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/btnLoginGoogle')
        google_btn.click()
        time.sleep(3)

        choose_acc = self.driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]')
        choose_acc.click()
        time.sleep(3)

        try:
            login_success = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/iconProfile')
            if(login_success.is_displayed()):
                print("Pengguna telah berhasil login")
        except:
            self.driver.implicitly_wait(5)
            print("Anda belum login, silakan login terlebih dahulu")
        time.sleep(5)
        

        numerasi_btn = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/button')
        numerasi_btn.click()
        time.sleep(3)

        mulai_btn = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/btnDataDanKetidakpastian')
        mulai_btn.click()
        time.sleep(5)

        actions = ActionChains(self.driver)
        #actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(959, 439)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(63, 422)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

        soal10 = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.LinearLayout[@content-desc="10"]/android.widget.TextView')
        soal10.click()
        time.sleep(3)
        self.scroll(2)

        next_btn = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/btnNext')
        next_btn.click()
        try:
            confirm_popup = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/confirm')
            if(confirm_popup.is_displayed()):
                print("Silakan konfirmasi submit jawaban")
        except:
            print("Anda telah submit, tanpa konfirmasi")
        time.sleep(3)

    
    def test_05_profile(self) -> None:
        self.driver.implicitly_wait(10)
        print("\nThe layout of the user's name on the profile page\n=======================================")
        
        email_field = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/txtEmail')
        email_field.send_keys("tsaqibsteam2@gmail.com")
        pass_field = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/txtPassword')
        pass_field.send_keys("123456")
        time.sleep(2)

        masuk_btn = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/btnMasuk')
        masuk_btn.click()
        time.sleep(3)

        try:
            login_success = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/iconProfile')
            if(login_success.is_displayed()):
                print("Pengguna telah berhasil login")
        except:
            self.driver.implicitly_wait(5)
            print("Anda belum login, silakan login terlebih dahulu")
        time.sleep(5)
        

        profile_btn = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/iconProfile')
        profile_btn.click()
        print("Halaman profile ditampilkan")
        time.sleep(8)

    
    def test_06_eyeicon(self) -> None:
        self.driver.implicitly_wait(10)
        print("\nThe password field \n=======================================")
        
        email_field = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/txtEmail')
        email_field.send_keys("tsaqibsteam2@gmail.com")
        pass_field = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/txtPassword')
        pass_field.send_keys("123456")
        time.sleep(2)

        try:
            view_pass = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/eyeicon')
            if(view_pass.is_displayed()):
                print("Pengguna telah berhasil melihat nilai password")
        except:
            self.driver.implicitly_wait(2)
            print("Lihat nilai password tidak tersedia")
        time.sleep(5)

    def test_vertical_scroll(self) -> None:
        print("="*20)
        print("\nRunning vertical scroll field test")
        
        try:
            self.driver.implicitly_wait(5)
            email_field = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/txtEmail')
            email_field.send_keys('areallyreallyreallylongemail@gmail.com')

            time.sleep(5)

        except Exception as e:
            assert False, e

    def test_back_button_logout(self) -> None:
        print("="*20)
        print("\nRunning back button on logout test")
        
        try:
            self.driver.implicitly_wait(5)
            
            email_field = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/txtEmail')
            password_field = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/txtPassword')

            email_field.send_keys('tsaqibsteam@gmail.com')
            password_field.send_keys('123456')

            masuk_button = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/btnMasuk')
            masuk_button.click()

            profile = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/iconProfile')
            profile.click()

            logout_button = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/btnLogout')
            logout_button.click()

            confirm_logout_button = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/btnYa')
            confirm_logout_button.click()
            time.sleep(3)

            self.driver.back()
            time.sleep(5)

        except Exception as e:
            assert False, e

    def test_back_button_tryout(self) -> None:
        print("="*20)
        print("\nRunning back button on tryout test")
        
        try:
            self.driver.implicitly_wait(5)
            
            email_field = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/txtEmail')
            password_field = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/txtPassword')

            email_field.send_keys('tsaqibsteam@gmail.com')
            password_field.send_keys('123456')

            masuk_button = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/btnMasuk')
            masuk_button.click()

            tryout_cat_button = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/button')
            tryout_cat_button.click()

            tryout_mulai_button = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/btnDataDanKetidakpastian')
            tryout_mulai_button.click()
            time.sleep(3)

            self.driver.back()
            time.sleep(5)

        except Exception as e:
            assert False, e

    def test_back_button_tryout_result(self) -> None:
        print("="*20)
        print("\nRunning back button on tryout results test")
        
        try:
            self.driver.implicitly_wait(5)
            
            email_field = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/txtEmail')
            password_field = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/txtPassword')

            email_field.send_keys('tsaqibsteam@gmail.com')
            password_field.send_keys('123456')

            masuk_button = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/btnMasuk')
            masuk_button.click()

            self.driver.implicitly_wait(5)
            tryout_cat_button = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/button')
            tryout_cat_button.click()

            tryout_mulai_button = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/btnDataDanKetidakpastian')
            tryout_mulai_button.click()
            
            # counter to count which question is it currently on
            count = 1
            
            while count <= 10:
                if count == 1:
                    time.sleep(5)
                
                scroll_count = 0
                while not (self.check_element_presence('com.salugan.cobakeluar:id/btnNext')):
                    scroll_count += 1
                    self.scroll()

                if count == 10:
                    while not (self.check_element_presence('com.salugan.cobakeluar:id/btnNext')):
                        self.scroll()
                    self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/btnNext').click()
                    time.sleep(3)
                    self.driver.back()

                # code below is to answer the answers available while looping thru the questions
                answer_options = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/answerOptionsContainer').find_elements(by=AppiumBy.CLASS_NAME, value='android.widget.LinearLayout')[:-1]

                for answer in answer_options:
                    answer.click()

                self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/btnJawab').click()
                self.driver.implicitly_wait(5)
                self.driver.back()

                for i in range(scroll_count):
                    self.scroll()
                
                self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/btnNext').click()
                count += 1

            time.sleep(5)

        except Exception as e:
            assert False, e

    def test_back_button_home_login(self) -> None:
        print("="*20)
        print("\nRunning back button on home and login page test\n")
        
        try:
            self.driver.implicitly_wait(5)
            
            email_field = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/txtEmail')
            password_field = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/txtPassword')

            email_field.send_keys('tsaqibsteam@gmail.com')
            password_field.send_keys('123456')

            masuk_button = self.driver.find_element(by=AppiumBy.ID, value='com.salugan.cobakeluar:id/btnMasuk')
            masuk_button.click()

            time.sleep(3)
            self.driver.back()

            time.sleep(3)
            self.driver.back()

            time.sleep(5)

        except Exception as e:
            assert False, e



if __name__ == '__main__':
    unittest.main()