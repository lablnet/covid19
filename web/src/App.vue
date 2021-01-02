<template>
<nav class="navbar navbar-expand-lg nav">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Covid19</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse justify-content-end" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
        <router-link class="nav-link" to="/">Home</router-link>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Chat Bot</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Deep Dive
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Map</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
  <router-view/>

  <footer class="footer text-center justify-content-center">
    <p class="content-about"><b>Disclaimer:</b> Error and Omissions expected</p>
    <p class="content-about text-danger">The testing capacity in Pakistan is very low, the real cases can be much higher.</p>
    <p class="content-about" style="font-size: 11px">
    Information displayed here is carefully calibrated and is mostly updated manually based on reporting of government officals on Website.
    </p>
    <p class="content-about mt-2">
      <ol>
        <li><router-link class="nav-link" to="/about">About</router-link></li>
        <li><router-link class="nav-link" to="/about">Feedback</router-link></li>
        <li><router-link class="nav-link" to="/about">Data Request</router-link></li>
      </ol>
    </p>
    <p class="content-about mt-2 mb-3">
      Copyright © 2020 - Developers
    </p>
  </footer>
</template>
