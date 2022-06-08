
from src.profile_scraper import ProfileScraper
from scripts.chrome_driver import ChromeDriver
from time import sleep
import os

class ArgSpace:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

cols_to_keep=['__typename', 'id', 'shortcode', 'display_url', 'owner', 'is_video',  'accessibility_caption', 'video_url', 'video_view_count',
            'edge_media_to_caption', 'edge_media_to_comment', 'nft_asset_info', 'product_type', 'edge_liked_by']


def test_profile_scraper_basic():
    scraper=ProfileScraper()

    args=ArgSpace(output_folder=os.getenv('OUTPUT_FOLDER'),
    username=os.getenv('TEST_IG_USER'),
    password=os.getenv('TEST_IG_PWD'),
    target_profile=os.getenv('TEST_TARGET_PROFILE'),
    max_iterations=1) # max_iterations is set to 1 in order to not make too many calls and get IG angry

    chrome_driver=ChromeDriver()

    proxy=chrome_driver.set_up_proxy()
    Driver=chrome_driver.set_up_driver(proxy=proxy)
    Driver=chrome_driver.make_IG_access(driver=Driver, ig_usr=args.username, ig_pass=args.password)
    sleep(2)
    raw_data=scraper.scrape(driver=Driver, proxy=proxy, args=args, save_raw_data=True)

    assert ~raw_data.empty
    Driver.quit()
    sleep(5)


def test_profile_scraper_clean_data():
    scraper=ProfileScraper()

    args=ArgSpace(output_folder=os.getenv('OUTPUT_FOLDER'),
    username=os.getenv('TEST_IG_USER'),
    password=os.getenv('TEST_IG_PWD'),
    target_profile=os.getenv('TEST_TARGET_PROFILE'),
    max_iterations=1) # max_iterations is set to 1 in order to not make too many calls and get IG angry

    chrome_driver=ChromeDriver()

    proxy=chrome_driver.set_up_proxy()
    Driver=chrome_driver.set_up_driver(proxy=proxy)
    Driver=chrome_driver.make_IG_access(driver=Driver, ig_usr=args.username, ig_pass=args.password)
    sleep(2)

    raw_data=scraper.scrape(driver=Driver, proxy=proxy, args=args, save_raw_data=True)
    Driver.quit()
    clean_data=scraper.parse_and_save_full_profile_raw_har(har=raw_data, args=args)
    assert ~raw_data.empty
    assert clean_data.columns == cols_to_keep
    sleep(5)