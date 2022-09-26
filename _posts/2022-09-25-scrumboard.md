---
description: "Graphic for our Scrum Team using HTML, CSS, & JS"
title: "Scrum Team"
badges: true
comments: true
categories: [scrum]
layout: post
---


<html>

<body>

  <div style="display: flex; width: 100%; flex-direction: row; justify-content: center; align-items: center;">

    <ul>
      <li>Scrum Master: Ethan Tran</li>
      <li>DevOPs: Rohin Sood</li>
      <li>Frontend Devs: Luna Iwazaki, Taiyo Iwazaki</li>
      <li>Backend Dev: Parav Salaniwal</li>
    </ul>
  </div>

  <div id="steps-container">
    
  </div>

</body>

<style>
  #steps-container {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    width: 100%;
    margin-top: 4px;
    gap: 4px;
    flex-grow: 4;
  }

  #step-box {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    padding-left: 6px;
    padding-right: 6px;
    border-radius: 8px;
    text-align: center;
  }

</style>

<script>
  var steps = ["Directions Given", "Assigning Jobs", "Splitting Workload Accordingly", "Planning Overview", "Deploy Project", "Finished Work"];

  var container = document.getElementById("steps-container");

  steps.forEach( (value, i) => {

    let num = document.createElement("h2");
    num.innerHTML = i + 1;

    let step = document.createElement("p");
    step.style.textAlign = "center";
    step.style.backgroundColor = "black";
    step.innerHTML = value;

    let box = document.createElement("div");
    box.setAttribute("id", "step-box");

    box.appendChild(num);
    box.appendChild(step);

    container.appendChild(box);
 
  } );

</script>

</html>

 

