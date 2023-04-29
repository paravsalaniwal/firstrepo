---
toc: true
layout: post
title: SASS Hacks
---
<style>
@mixin button-styles($color, $font-size) {
  font-size: $font-size;
  padding: 20px 40px;
  color: white;
  text-shadow: 1px 1px 1px rgba(0, 0, 0, 0.4);
  border: none;
  border-radius: 20px;
  cursor: pointer;
  background-color: $color;
  transition: all 0.2s ease-in-out;
}

.primary-button {
  @include button-styles(#007bff, 1.5em);
  &:hover {
    transform: scale(1.1);
  }
}

.secondary-button {
  @include button-styles(#6c757d, 1.2em);
  &:hover {
    transform: scale(1.1);
  }
}

</style>

<div>
  <center><button class="primary-button">Mr.Yeung is the better CS Teacher</button></center>
</div>
<div>
  <center><button class="secondary-button">Mr.Mort is the better CS Teacher</button></center>
</div>
