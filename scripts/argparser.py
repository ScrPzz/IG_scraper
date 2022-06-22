""" Keyboard flags parser"""
import argparse


class ArgParser:
    """Argaparser wrapper class"""

    def __init__(self):
        pass

    @classmethod
    def likes_scraper_read_input(self):
        """Input reader for likes and comments scraper"""
        parser = argparse.ArgumentParser("Instagram likes scraper")
        parser._action_groups.pop()
        required = parser.add_argument_group("required arguments")
        optional = parser.add_argument_group("optional arguments")

        required.add_argument("-u", "--username", help="IG username", required=True)
        required.add_argument("-p", "--password", help="IG password", required=True)
        required.add_argument(
            "-t", "--target_post", help="Target IG post url", required=True
        )

        optional.add_argument(
            "-o",
            "--output_folder",
            help="Folder in which store the scrapes",
            required=False,
            default="./output",
        )
        optional.add_argument(
            "-N",
            "--max_iterations",
            help="Max number of iterations",
            required=False,
            default=5,
        )
        # Add load urls from file option
        optional.add_argument(
            "-F",
            "--source_file",
            help="Get urls from a txt",
            required=False,
            default=None,
        )

        return parser.parse_args()

    @classmethod
    def profile_scraper_read_input(self):
        """Input reader for full profile scraper"""
        parser = argparse.ArgumentParser("Instagram profile scraper")
        parser._action_groups.pop()
        required = parser.add_argument_group("required arguments")
        optional = parser.add_argument_group("optional arguments")

        required.add_argument("-u", "--username", help="IG username", required=True)
        required.add_argument("-p", "--password", help="IG password", required=True)
        required.add_argument(
            "-t", "--target_profile", help="Target IG profile url", required=True
        )

        optional.add_argument(
            "-o",
            "--output_folder",
            help="Folder in which store the scrapes",
            required=False,
            default="./output",
        )
        optional.add_argument(
            "-N",
            "--max_iterations",
            help="Max number of iterations",
            required=False,
            default=3,
        )

        return parser.parse_args()
