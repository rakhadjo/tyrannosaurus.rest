# 🦕 <i>tyrannosaurus.rest</i> 🦖
The Dinosaur Rest API, because why the hell not? <br /><br />
The word 'dinosaur' originates from the Greek words <i>deinos</i> meaning 'terrible' and <i>sauros</i> meaning 'lizard'.
Hence the word 'dinosaur' actually means 'terrible lizard'. That said, there are a lot of misconceptions today regarding the actual creatures that the
general public mislabel as 'dinosaur' (e.g. ichthyosaurs, mosasaurs, pterosaurs etc. are not actually 'dinosaurs' at all.) <br /><br />
I hope by categorizing information in this API through endpoints, a clearer picture can be painted regarding their mislabeling.

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

Currently supported endpoints to substitute `{dino-name}`:
```
 .
 ├── x
 ├── x
 ├── x
 ├── x
 └── x
```
#### Categorized by Era


#### Return Type (to be done later)
In all cases, the return type will be as follows:
```json
{
  "name": "dino-name",
  "diet": "food-type",
  "era": "jurrasic, triassic, etc."
}
```

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
