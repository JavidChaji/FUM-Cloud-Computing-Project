<a name="readme-top"></a>

[![Contributors][Contributors-Shield]][Contributors-URL]
[![Forks][Forks-Shield]][Forks-URL]
[![Stargazers][Stars-Shield]][Stars-URL]
[![Issues][Issues-Shield]][Issues-URL]
[![MIT License][License-Shield]][License-URL]

[![LinkedIn][LinkedIn-Shield]][-LinkedIn-URL]
[![LinkedIn][LinkedIn-Shield]][-LinkedIn-URL]
[![LinkedIn][LinkedIn-Shield]][Javid-LinkedIn-URL]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/javidchaji/Cloud-Computing-Project">
    <img src="images/Docker-Logo.png" alt="Docker-Logo" height="80">
  </a>
  <a href="https://github.com/javidchaji/Cloud-Computing-Project">
    <img src="images/Docker-Compose-Logo.png" alt="Docker-Compose-Logo" height="80">
  </a>
  <a href="https://github.com/javidchaji/Cloud-Computing-Project">
    <img src="images/Kubernetes-Logo.png" alt="Kubernetes-Logo" height="80">
  </a>

  <h2 align="center">Cloud Computing Project</h2>

  <p align="center">
    Hey !!
    <br />
    In This Repo We are going to Learn Some Docker, Docker-Compose And Kuberneties together
    <br />
    <a href="https://github.com/javidchaji/Cloud-Computing-Project"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/javidchaji/Cloud-Computing-Project/issues">Report Bug</a>
    ·
    <a href="https://github.com/javidchaji/Cloud-Computing-Project/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-Repository">About The Repository</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
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



<!-- ABOUT THE PROJECT -->
## About The Repository

Ferdowsi University of Mashhad Cloud Computing Project

[![Product Name Screen Shot][Product-Screenshot]](https://example.com)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

Technologies and Tools Utilized in this Project

* [![Docker][Docker]][Docker-url]
* [![Linux][Linux]][Linux-url]
* [![Kubernetes][Kubernetes]][Kubernetes-url]
* [![Nginx][Nginx]][Nginx-url]
* [![Python][Python]][Python-url]
* [![MySQL][MySQL]][MySQL-url]
<!-- * [![Docker-Compose][Docker-Compose]][Docker-Compose-url] -->


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites
#### 1. Installing Docker and Docker-Compose
* **Note 1**: Replace **version** with the latest version number from the Docker Engine - Community repository.
* **Note 2**: For X86_64 Architecture CPUs use amd64 in place of **arch** if you are using a different architecture than x86_64, you can find the correct arch by running `uname -m` on your machine.

    * ### In Ubuntu
      1. Update Your apt

          ```sh
          sudo apt-get update
          ```
      2. Download Docker Desktop for Ubuntu

          ```sh
          wget https://desktop.docker.com/linux/main/amd64/docker-desktop-<version>-<arch>.deb
          ```
      3. Installing Docker Desktop
          
            ```sh
            sudo apt install ./docker-desktop-<version>-<arch>.deb
            ```
    * ### In Arch Linux
      1. Update Your Pacman

          ```sh
          sudo pacman -Syu
          ```
      2. Downloading and Installing Docker and Docker-Compose Plugin for Arch

          ```sh
          sudo pacman -S docker docker-compose
          ```

    * ### In Windows Command Prompt
      1. Download Docker Desktop With This Command

          ```sh
          Invoke-WebRequest https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe
          ```
      2. Type Command Below For installing Docker Desktop

          ```sh
          start /w "" "Docker Desktop Installer.exe" install
          ```

### Installation

installing and setting up the app 

1. Clone the repo

    ```sh
    git clone https://github.com/javidchaji/Cloud-Computing-Project.git
    ```
2. Install ... packages

    ```sh
    ... install
    ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

<!-- Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources. -->

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

1. >Choose a Webserver image from [Docker Hub](https://hub.docker.com/) (Like: Nginx, Apache, etc.)
    * **Nginx** is the one we are going to use in this project.
    * Downloading WebServer Image From Docker Hub
      - [ ] Downloading Nginx Image From Docker Hub
2. >Writing Dockerfile For WebServer That Do One of these Tasks : 
    >1. >Acting as Reverse Proxy for a simple application.
    >2. >Hosting an HTML Page.

  - >*Note* : First Task Can Have Extra Points For Architecture and Richer Configuration

      1. >WebServer must be able to host a Content of a Folder Outside of the Container
          - [x] Writing Dockerfile that can host a Content of a Folder Outside of the Container
      2. >Choosing a way of Configuring the WebServer (Like: copying in image, mounting a volume, etc.)
          - [x] ... is the one we are going to use in this project.

3. >Choose a Database image from [Docker Hub](https://hub.docker.com/) (Like: Elasticsearch, MySQL, MongoDB, etc.)
    * **MySQL** is the one we are going to use in this project.
    * Downloading Database Image From Docker Hub
      - [x] Downloading MySQL Image From Docker Hub
  - >*Note* : The related image configuration must written in docker-compose.yml file that have these four features :
      >1. >The Configuration file must be Stateful (Meaning that the data will be saved even if the container is removed)
      >2. >Each container must use Limited amount of resources (Like: CPU, Memory, etc.)
      >3. >For choosen database Define a separate username and password
      >4. >Need to run automatically after each system restart.
      - [x] Downloading The Database Image From Docker Hub
      - [x] The Related image Configuration must write 
4. >By using Pervious Step Dockerfile do the build opration note that both images must run together
    - [ ] Writing docker-compose.yml File 
5. >Push the built image to Docker Hub
    - [ ] Pushing The Built Image To Docker Hub
    - [ ] Puting Docker Hub Image Link In issue Phase 1

See the [open issues](https://github.com/javidchaji/Cloud-Computing-Project/issues) for a full list of proposed features (and known issues).

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

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Mohadese Behzadi - [@](https://twitter.com/) - @gmail.com

Zahra Dehghan - [@](https://twitter.com/) - @gmail.com

Javid Chaji - [@JavidChaji](https://twitter.com/JavidChaji) - javid.chaji@gmail.com

Project Link: [https://github.com/javidchaji/Cloud-Computing-Project](https://github.com/javidchaji/Cloud-Computing-Project)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Docker-Compose](https://docs.docker.com/compose/)
* [Dockerfile](https://docs.docker.com/engine/reference/builder/)
* [Choose an Open Source License](https://choosealicense.com)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
<!-- * [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet) -->
<!-- * [GitHub Pages](https://pages.github.com) -->
<!-- * [Font Awesome](https://fontawesome.com) -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
<!-- https://ileriayo.github.io/markdown-badges/ -->

<!-- Contributors -->
[Contributors-Shield]: https://img.shields.io/github/contributors/javidchaji/Cloud-Computing-Project.svg?style=for-the-badge

[Contributors-URL]: https://github.com/javidchaji/Cloud-Computing-Project/graphs/contributors


<!-- Forks -->
[Forks-Shield]: https://img.shields.io/github/forks/javidchaji/Cloud-Computing-Project.svg?style=for-the-badge

[Forks-URL]: https://github.com/javidchaji/Cloud-Computing-Project/network/members


<!-- Stars -->
[Stars-Shield]: https://img.shields.io/github/stars/javidchaji/Cloud-Computing-Project.svg?style=for-the-badge

[Stars-URL]: https://github.com/javidchaji/Cloud-Computing-Project/stargazers


<!-- Issues -->
[Issues-Shield]: https://img.shields.io/github/issues/javidchaji/Cloud-Computing-Project.svg?style=for-the-badge

[Issues-URL]: https://github.com/javidchaji/Cloud-Computing-Project/issues


<!-- License -->
[License-Shield]: https://img.shields.io/github/license/javidchaji/Cloud-Computing-Project.svg?style=for-the-badge

[License-URL]: https://github.com/javidchaji/Cloud-Computing-Project/blob/master/LICENSE


<!-- LinkedIn -->
[LinkedIn-Shield]: https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white

[-LinkedIn-URL]: https://linkedin.com/in/

[-LinkedIn-URL]: https://linkedin.com/in/

[Javid-LinkedIn-URL]: https://linkedin.com/in/javidchaji


<!-- Product-Screenshot -->
[Product-Screenshot]: images/screenshot.png


<!-- Kubernetes -->
[Kubernetes]: https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white

[Kubernetes-URL]: https://kubernetes.io/


<!-- Docker  -->
[Docker]: https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white

[Docker-URL]: https://www.docker.com/


<!-- Docker-Compose -->
[Docker-Compose]: https://img.shields.io/badge/dockercompose-35495E?style=for-the-badge&logo=dockercompose&logoColor=4FC08D

[Docker-Compose-URL]: https://docs.docker.com/compose/


<!-- python -->
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54

[Python-URL]: https://www.python.org/


<!-- Nginx -->
[Nginx]: https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white

[Nginx-URL]: https://www.nginx.com/


<!-- Linux -->
[Linux]: https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black

[Linux-URL]: https://www.linux.org/


<!-- MySQL -->
[MySQL]: https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white

[MySQL-URL]: https://www.mysql.com/
