from pytubefix import YouTube, Channel
from pytubefix.cli import on_progress
from urllib import parse
from argparse import ArgumentParser

parser = ArgumentParser(prog="Youtube video downloader", description="Download Youtube videos")
parser.add_argument("-c", "--channel", help="the channel url", required=True)
parser.add_argument("-o", "--output", help="the output folder path", required=True)
args = parser.parse_args()

channel_url = parse.quote(args.channel)
save_path = args.output

def download_video(url):
	yt = YouTube(url, on_progress_callback=on_progress)
	print(yt.title)
	ys = yt.streams.get_highest_resolution()
	ys.download()

def download_all_channel_videos(channel_url, output_path):
	c = Channel(channel_url)

	for video in c.videos[1:3]:
		video.streams.get_highest_resolution().download(output_path=output_path)

download_all_channel_videos(channel_url, save_path)
