import os
import pytest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

'''
This code defines a pytest fixture called browser that sets up and tears down a 
Chrome WebDriver instance for web automation testing. Let's break it down:

The @pytest.fixture(scope="module") decorator marks this function as a fixture 
that will be shared across all tests within a module. This means the browser will
 be launched once for all tests in the module rather than for each test.

A common "gotcha" here is the difference between scope="module" vs scope="function".
 With "module" scope, tests share the same browser instance which is faster but could 
 lead to state bleeding between tests if not managed carefully.

You might want to improve this code by:

Adding error handling around the driver initialization
Making the chrome_path configurable through environment variables
Adding explicit waits or timeouts for better reliability 
'''
@pytest.fixture(scope="module")
def browser():
    # Get Chrome path from environment variable or use default
    #chrome_path = os.getenv('CHROME_BINARY_PATH', 
    #    "/home/egaliza/WORKSPACE-PYTHON/ALURA-Scripting-automacao-tarefas/dash/chrome-linux64/chrome")
    #driver_path = os.path.join(os.path.dirname(__file__), "drivers", "chromedriver")
    #driver_path = os.getenv('CHROMEDRV_BINARY_PATH', '/usr/bin/chromedriver')
    
    # if not os.path.exists(chrome_path):
    #     raise FileNotFoundError(f"Chrome binary not found at {chrome_path}")
    
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.binary_location = chrome_path
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")

    try:
        #service = webdriver.ChromeService(executable_path=driver_path)
        #driver = webdriver.Chrome(service=service, options=chrome_options)
        driver = webdriver.Chrome(options=chrome_options)
        print(f"Chrome started successfully")
        '''
        The yield statement is a crucial part - it:
        Returns the driver to the test that needs it
        Marks where the teardown code begins
        After the test completes, execution continues after the yield
        '''
        yield driver
    except WebDriverException as e:
        raise RuntimeError(f"Failed to start Chrome: {e}")
    finally:
        '''
        Finally, driver.quit() ensures the browser is properly closed after all tests 
        are complete, preventing memory leaks and orphaned browser processes.
        '''
        if 'driver' in locals():
            driver.quit()
            print("Chrome stopped successfully.")