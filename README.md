# Google Photos Matcher (Linux fork) (v 1.2)

Simple executable to match metadata from JSONs to original images/videos.

Same work than [MetadataFixer](https://metadatafixer.com/pricing) but its free!

## Wiki 📖

When you download the images from google photos, they lose some metadata such as the date and the coordinates in which they were taken.

This algorithm is able to match this information in the image/video from the downloaded JSONs

## Usage

1. Download your _Google Photos_ media from [Takeout](https://takeout.google.com/)

2. Clone this repository and run `python3 cli.py <path>`

    - Optionally run with `--suffix` or `-s` to add a custom file suffix

3. Matched images/videos will be on directory _-MatchedMedia_ inside the same path

## FAQs

### Why is there another folder called _EditedRaw_?

Images and videos edited from _Google Photos's_ editor will have 2 different versions: 

  1. Edited version
  2. Original version
  
Edited version will be stored in _MatchedMedia_ while original in _EditedRaw_

### Why some images/videos stay unmatched?

Sometimes, the algorithm does not recognize the names of the images due to the presence of some special characters. These files will remain in the same folder. To fix it, rename both the JSON and the original file.

#### For example: 

  - Algorithm fails with image _%E&xample.jpg_


#### Solution

1. Rename _%E&xample.jpg_ to _Example.jpg_ and _%E&xample.json_ to _Example.json_ 

2. Open JSON and change title attribute to _Example.jpg_

3. Run again

## Contributors ✒️

* **anderbggo** - Author
* **Freepik** - Icon creator
* **UvixCreative** - Forked and modified to run on Linux

## Donations💰

See the [original project](https://github.com/mcgrawia/GooglePhotosMatcher) for donation links
