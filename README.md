# Food GAN

This repo implements a DCGAN and a WGAN to generate novel images of food.

## Data
I [scraped](https://github.com/rtlee9/recipe-box) ~125,000 recipes from various websites for use in this model. Each recipe consists of:

* A recipe title
* A list of ingredients
* Preparation instructions
* An image of the prepared recipe (missing for ~40% of recipes collected)

These GANs were fitted on the recipe images; they did not utilize the recipe's title, ingredients list, or instructions.
