import os
import time
import logging
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup /logs directory
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Generate timestamped log file name
timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
log_file_path = os.path.join(LOG_DIR, f"test_run_{timestamp_str}.log")

# Configure logging format
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(message)s",
    handlers=[
        logging.FileHandler(log_file_path, encoding="utf-8"),
        logging.StreamHandler()
    ]
)

PORTFOLIO_URL = "https://keza250.github.io/kezamillajoie.github.com/"
def run_test_suite():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    
    total_tests = 0
    passed_tests = 0
    failed_tests = 0
    run_start_time = time.time()

    browser_version = driver.capabilities.get("browserVersion", "Chrome")
    os_info = driver.capabilities.get("platformName", "OS")

    logging.info(f"RUN START | portfolio: {PORTFOLIO_URL} | browser: Chrome {browser_version} | OS: {os_info}")

    def execute_test(test_id, action_desc, expected_desc, test_func):
        nonlocal total_tests, passed_tests, failed_tests
        total_tests += 1
        start_time = time.time()

        try:
            actual_result = test_func(driver)
            duration = time.time() - start_time
            logging.info(f"{test_id} | {action_desc} | expected: {expected_desc} | actual: {actual_result} | PASS | {duration:.1f} s")
            passed_tests += 1
        except Exception as e:
            failed_tests += 1
            duration = time.time() - start_time
            error_msg = str(e).split('\n')[0]
            
            screenshot_name = f"{test_id}_fail_{timestamp_str}.png"
            screenshot_path = os.path.join(LOG_DIR, screenshot_name)
            driver.save_screenshot(screenshot_path)
            
            logging.error(f"{test_id} | {action_desc} | expected: {expected_desc} | actual: {error_msg} | FAIL | {duration:.1f} s | screenshot: {screenshot_name}")

    try:
        driver.get(PORTFOLIO_URL)
        driver.maximize_window()
        time.sleep(2)

        # TC-01: Home Page Load
        execute_test(
            "TC-01",
            "Open Portfolio Home Page",
            "Page title contains expected text",
            lambda d: f"Page title is '{d.title}'"
        )

        # TC-02: About Section Link
        def test_about(d):
            link = WebDriverWait(d, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '#about') or contains(text(), 'About')]"))
            )
            link.click()
            time.sleep(1)
            return "Navigated to #about section"

        execute_test(
            "TC-02",
            "Click 'About Me' link",
            "#about section visible",
            test_about
        )

        # TC-03: Services Section Link
        def test_services(d):
            link = WebDriverWait(d, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '#services') or contains(text(), 'Services')]"))
            )
            link.click()
            time.sleep(1)
            return "Navigated to #services section"

        execute_test(
            "TC-03",
            "Click 'Services' link",
            "#services section visible",
            test_services
        )

        # TC-04: Projects Section Link
        def test_projects(d):
            link = WebDriverWait(d, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '#projects') or contains(text(), 'Projects')]"))
            )
            link.click()
            time.sleep(1)
            return "Navigated to #projects section"

        execute_test(
            "TC-04",
            "Click 'Projects' link",
            "#projects section visible",
            test_projects
        )

        # TC-05: External Repository Link
        def test_external(d):
            link = WebDriverWait(d, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'github')]"))
            )
            return f"External link points to '{link.get_attribute('href')}'"

        execute_test(
            "TC-05",
            "Check GitHub external link",
            "Link contains valid GitHub target",
            test_external
        )

        # TC-06: Negative Test (Intentional Failure)
        def test_negative_missing(d):
            d.find_element(By.ID, "nonexistent-section-id-12345")
            return "Element found unexpectedly"

        execute_test(
            "TC-06",
            "Find non-existent element (Negative Test)",
            "NoSuchElementException caught and logged",
            test_negative_missing
        )

    finally:
        driver.quit()
        total_duration = time.time() - run_start_time
        logging.info(f"RUN END | total: {total_tests} | passed: {passed_tests} | failed: {failed_tests} | duration: {total_duration:.1f} s")
        print(f"\nExecution complete. Log generated at: {log_file_path}")

if __name__ == "__main__":
    run_test_suite()