class StartPageConst:
    """Stores constants related to start page"""
    #confirm age YES/NO
    ADULT_WINDOW_XPATH = './/div[@class="sc-6e5c79b5-1 gMeQCW"]'
    YES_BUTTON_XPATH = './/a[@class="sc-6e5c79b5-4 gwJZmj"]'
    NO_BUTTON_XPATH = './/a[@href="https://www.google.com"]'

    START_PAGE_BESTSELERS_XPATH = './/h2[@class="sc-f91cb35f-1 bncsWx"]'
    START_PAGE_BESTSELERS_TEXT = 'Бестселери'

    MENU_XPATH = './/div[@class="sc-86c356ae-3 gSawTJ"]'
    IMPORT_XPATH ='.//a[@href="/ua/sobstvennyy-import"]'

    LOGIN_XPATH = './/div[@class ="sc-4b6ede46-3 exReQB"]'
    # SIGN_IN_EMAIL_FIELD_XPATH = ".//input[@id='emailId']"
    # SIGN_IN_PASSWORD_FIELD_XPATH = ".//input[@id='passwordId']"
    SIGN_IN_BUTTON_XPATH = './/div[@class="sc-3bc511a6-11 sc-3bc511a6-14 fGkcVF kUdgaJ"]'
    ERROR_LOGIN_XPATH = './/div[@class="sc-ed3d24c3-0 fgqYqX"]'
    ERROR_LOGIN_TEXT = 'Введіть пароль'

    SIGN_UP_WINDOW_XPATH = './/div[@class="sc-3bc511a6-10 emBIAA"]'
    SIGN_UP_USERNAME_FIELD_XPATH = './/input[@id="firstNameId"]'
    SIGN_UP_SURNAME_FIELD_XPATH = './/input[@id="lastNameId"]'
    SIGN_UP_EMAIL_FIELD_XPATH = './/input[@name="email"]'
    SIGN_UP_PASSWORD_FIELD_XPATH = ".//input[@id='passwordId']"
    SIGN_UP_CONFIRM_PASSWORD_FIELD_XPATH = ".//input[@id='passwordConfirmId']"
    SIGN_UP_BUTTON_XPATH = './/div[@class="sc-3bc511a6-11 sc-3bc511a6-16 fGkcVF bPfAyg"]'

    ERROR_EMPTY_EMAIL_XPATH = './/div[@class="sc-ed3d24c3-0 fgqYqX"]'
    ERROR_EMPTY_EMAIL_TEXT = 'Введіть пошту'

    PRODUCT_INFO_XPATH = './/a[@href="/ua/product/liker-dead-mans-fingers-dmf-raspberry-rum-cream-liqueur-17-07l"]'




