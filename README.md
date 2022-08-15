<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GNU License][license-shield]][license-url]
[![Python3][Python3]][Python-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- PROJECT LOGO -->
<div align="center">
<a href="https://github.com/chrisddr77/darksouls_text_generator"></a>
<h1 align="center">Dark Souls Text Generator</h1>
  <p align="center">
    Python app to generate Dark Souls style text.
    <br />
    <br />
    <a href="https://github.com/chrisddr77/darksouls_text_generator/issues">Report Bug</a>
    ·
    <a href="https://github.com/chrisddr77/darksouls_text_generator/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<br />
<br />
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">Screenshots</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- Screenshots -->
## Screenshots

[![Screenshot 1][product-screenshot-1]]()
[![Screenshot 2][product-screenshot-2]]()
[![Screenshot 3][product-screenshot-3]]()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

You will only need a few things to get set up.

### Prerequisites
* Python 3 (Only tested with 3.9+)


* Trajan Pro Regular font - [Download it from fontsgeek](https://fontsgeek.com/fonts/Trajan-Pro-Regular)


* pillow
  ```sh
  pip install pillow
  ```
  


### Installation

1. Clone the repo OR [Download it as a zip][zip-download-url] and extract it
    ```sh
   git clone https://github.com/chrisddr77/darksouls_text_generator.git
   ```
2. Copy the `Trajan Pro Regular.ttf` font into the same directory as `main.py`
3. Run `python main.py`

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

#### Keyboard:
* `Space` key: Generates a random image with random 3-word text
* `S` key: Saves the current image to the `/generated` folder as `{generated_text}.png`
* `R` key: Resets the input text to its default value
* `B` key: Randomly selects a different background


* These keys only work when the input text is its default value `{adjective} {noun} {past tense verb}`:
  * `1` key: Re-generates the 1st word
  * `2` key: Re-generates the 2nd word
  * `3` key: Re-generates the 3rd word

<br/>

#### Text input:
The text input field at the top of the window allows for user inputted text to be displayed (Note: This disables the `1`, `2`, `3` keys).
Variables can be used to get random nouns, adjectives, or past tense verbs.
* `{adjective}`
* `{noun}`
* `{past tense verb}`

Example text input using variables:
* `Dogs are {adjective}`
* `The {noun} is {adjective}`
* `They {past tense verb} at the {noun}`





<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Re-generate the 1st, 2nd, and 3rd words with the `1`, `2`, `3` keys.
- ~~[ ] Allow 2 or 3 word text generation (eg. noun verbed OR adjective noun verbed).~~ (Covered by user inputted text)
- [x] Accept user inputted text.
- [x] Display keybindings to the user.
- [ ] Add scrolling back to previously generated images / text.

See the [open issues](https://github.com/chrisddr77/darksouls_text_generator/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GNU General Public License v3.0. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Christian Johnsten - crjohnsten@gmail.com

Project Link: [https://github.com/chrisddr77/darksouls_text_generator](https://github.com/chrisddr77/darksouls_text_generator)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* Inspired by the [@nounverbed](https://twitter.com/nounverbed) Twitter bot created by [@mrfb](https://twitter.com/mrfb)
* Backgrounds were screen-grabbed from a [Dark Souls 3 Walkthrough on YouTube](https://www.youtube.com/playlist?list=PLgPhYhf1rAvGyvo8JRKL53iBqJQbbqMJA) created by [Tselel Leb](https://www.youtube.com/channel/UCsUo1BrpZphLg8dfoYHNlGA)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/chrisddr77/darksouls_text_generator.svg?style=for-the-badge
[contributors-url]: https://github.com/chrisddr77/darksouls_text_generator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/chrisddr77/darksouls_text_generator.svg?style=for-the-badge
[forks-url]: https://github.com/chrisddr77/darksouls_text_generator/network/members
[stars-shield]: https://img.shields.io/github/stars/chrisddr77/darksouls_text_generator.svg?style=for-the-badge
[stars-url]: https://github.com/chrisddr77/darksouls_text_generator/stargazers
[issues-shield]: https://img.shields.io/github/issues/chrisddr77/darksouls_text_generator.svg?style=for-the-badge
[issues-url]: https://github.com/chrisddr77/darksouls_text_generator/issues
[license-shield]: https://img.shields.io/github/license/chrisddr77/darksouls_text_generator.svg?style=for-the-badge
[license-url]: https://github.com/chrisddr77/darksouls_text_generator/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/christian-johnsten
[product-screenshot-1]: screenshots/screenshot1.png
[product-screenshot-2]: screenshots/screenshot2.png
[product-screenshot-3]: screenshots/screenshot3.png
[Python3]: https://img.shields.io/badge/Python%203-306998?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://python.org/
[zip-download-url]: https://github.com/chrisddr77/darksouls_text_generator/archive/refs/heads/main.zip
