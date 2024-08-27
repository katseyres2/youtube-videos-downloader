from pytubefix import YouTube, Channel
from pytubefix.cli import on_progress
from urllib import parse
from argparse import ArgumentParser
import datetime as dt

parser = ArgumentParser(prog="Youtube video downloader", description="Download Youtube videos")
parser.add_argument("-c", "--channel", help="the channel url", required=True)
parser.add_argument("-o", "--output", help="the output folder path", required=True)
parser.add_argument("-d", "--days", help="number of days before today you can download videos", required=True)
args = parser.parse_args()

channel_url = parse.quote(args.channel)
save_path = args.output
days = int(args.days)

def download_video(url):
	yt = YouTube(url, on_progress_callback=on_progress)
	print(yt.title)
	ys = yt.streams.get_highest_resolution()
	ys.download()

def download_all_channel_videos(channel_url:str, output_path:str, max_previous_days:int):
	c = Channel(channel_url)

	for video in c.videos:
		videoEpoch = dt.datetime.timestamp(video.publish_date)
		currentEpoch = dt.datetime.timestamp(dt.datetime.now())
		days = (currentEpoch - videoEpoch) / 60 / 60 / 24

		if days > max_previous_days:
			break

		print("---------------")
		print(f"Publish date                                          : {video.publish_date}")
		print(f"Title                                                 : {video.title}")
		print(f"Duration in days between now and the video publication: {days} day(s)")
		print(f"Max duration between now and the video publication    : {max_previous_days} day(s)")

		video.streams.get_highest_resolution().download(output_path=output_path)

download_all_channel_videos(channel_url, save_path, days)
