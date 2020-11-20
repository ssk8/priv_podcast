import click
from google_drive_downloader import GoogleDriveDownloader as gdd


@click.command()
@click.argument('file_id')
def download(file_id):
    gdd.download_file_from_google_drive(file_id=file_id,
                                    dest_path=f'assets/{file_id}.mp3')

if __name__ == "__main__":
    download()
