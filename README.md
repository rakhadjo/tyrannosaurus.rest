# 🦕 <i>tyrannosaurus.rest</i> 🦖
[![Build Status](https://travis-ci.com/rakhadjo/tyrannosaurus.rest.svg?branch=master)](https://travis-ci.com/rakhadjo/tyrannosaurus.rest)

The Dinosaur Rest API, because why the hell not? <br /><br />
The word 'dinosaur' originates from the Greek words <i>deinos</i> meaning 'terrible' and <i>sauros</i> meaning 'lizard'.
Hence the word 'dinosaur' actually means 'terrible lizard'. That said, there are a lot of misconceptions today regarding the actual creatures that the
general public mislabel as 'dinosaur' (e.g. ichthyosaurs, mosasaurs, pterosaurs etc. are not actually 'dinosaurs' at all.) <br /><br />
I hope by categorizing information in this API through endpoints, a clearer picture can be painted regarding their mislabeling.

## Usage & Deploying

Assuming you've got `npm` and `Node` installed on your machine: <br />
1. `git clone https://github.com/rakhadjo/tyrannosaurus.rest.git`
2. `cd tyrannosaurus.rest`
3. `npm install`
4. `npm start`

By default I set the app to run on `localhost` port `1212`

### Tech Stack

ExpressJS for the API, JEST for unit testing, Python for Web Scraping

## Endpoints

tyrannosaurus.rest only accepts `GET` requests.
No authentication has been planned yet for this project.
Simply perform an HTTP `GET` request on the following endpoints to receive your content requests.
Data will be returned in the `json` format. More on this later.

### Dinosaur Information

There are two ways of getting the dinosaur information. <br>

#### Unordered, uncategorized

The first way is to simply substitute the dinosaur name:
`GET (host)/dinosaur/{dino-name}`
<br />

Currently supported endpoints to substitute `{dino-name}` can be found in [`static_content/endpoints.js`](./static_content/endpoints.js)

#### Categorized by Era

...needs work...

#### Return Type

In most cases, the return type will be as follows:

```json
{ 
   "name": "",
   "is_dino": "",
   "diet": "",
   "era": "",
   "found": "",
   "avg_weight_kg": "",
   "avg_length_m": "",
   "movement": ""
}
```
Data is retrieved from `dinosaurs.js` supposedly located in the root directory. 
### Developer

#### `/about`

Some meta-information of the API, developer, etc.

#### `/endpoints`

Returns the endpoints, and their descriptions.

### Random

#### `/movies`

List of Movies containing the general public understanding of what dinosaurs are 😒

#### `/random`

Returns some random dinosaur entry

#### `/dinobots`

Transformers Reference, they're essentially Autobots that can transform to prehistoric creatures.

#### `/sounds/{identifier}`

Me trying my best to represent each of their sounds with what I can do with my keyboard.
Will return `404` if empty
