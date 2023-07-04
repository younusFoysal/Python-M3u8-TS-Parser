
# 720p  = 1280 x 720
# 1080p = 1920 x 1080
# 1440p = 2560 x 1440
# 2160p = 3840 x 2160
# 4320p = 7680 x 4320

# Downloadding Master Playlist as Master
import urllib.request
import re
import os

# Creating MasterPlaylist Folder
if not os.path.exists("MasterPlaylist"):
    os.makedirs("MasterPlaylist")

# Downloadding Master Playlist as 01_Master
PathM3U = 'https://player.vimeo.com/external/159463108.m3u8?s=d41bea2a0d7223e3bd161fcb549b2c668437f1c9&oauth2_token_id=410160086'
NameM3U = "01_Master.m3u"
# Download the file from `url` and save it locally under `file_name`:
urllib.request.urlretrieve(PathM3U, NameM3U)

# Matching Higher Resolution and selecting its URL
ResolutionMatchRegex = '(.*RESOLUTION=1920x1080.*)[\r\n]+([^\r\n]+)'
RawM3u = open(NameM3U, 'r')
RawM3uText = RawM3u.read()
ResolutionMatch = re.findall(ResolutionMatchRegex, RawM3uText)[0]

# Writing Regex Match to 02_Master.m3u
StringMatchFile = open('02_Master.m3u', 'w')
StringMatchFile.write(ResolutionMatch[1])
StringMatchFile.close()

# Downloadding Chop Playlist as 03_Master.m3u
PathM3U = ResolutionMatch[1]
NameM3U = "03_Master.m3u"
# Download the file from `url` and save it locally under `file_name`:
urllib.request.urlretrieve(PathM3U, NameM3U)

# Matching Filename and extention
ExtensionMatchRegex = '.*\/'
URLFile = open('02_Master.m3u', 'r')
URLText = URLFile.read()
ExtensionMatch = re.findall(ExtensionMatchRegex, URLText)[0]

# Writing Regex Match (without filename and extension)to 04_Master.m3u
URLExtentionFile = open('04_Master.m3u', 'w')
URLExtentionFile.write(ExtensionMatch)
URLExtentionFile.close()

# Opening 04_Master.m3u to take url pattern
URLFile = open('04_Master.m3u', 'r')
URLText = URLFile.read()

# opening 04_Master.m3u Segment File
with open('03_Master.m3u', 'r') as playlist:
    ts_filenames = [line.rstrip() for line in playlist
                    if line.rstrip().endswith('.ts')]
StringMatchFile = open('MasterPlaylist/01_Master.m3u8', 'w')

for line in ts_filenames:
    StringMatchFile.write(URLText)
    StringMatchFile.write(line)
    StringMatchFile.write("\n")

# Deleting 01_Master.m3u, 02_Master.m3u, 03_master.m3u, 04_master.m3u
os.remove('01_Master.m3u')
os.remove('02_Master.m3u')
os.remove('03_Master.m3u')
os.remove('04_Master.m3u')
