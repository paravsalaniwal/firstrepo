---
toc: false
layout: post
description: Binary Calculator Input & Output
title: Binary Calculator
---

<html>
    <head>
        <style>
             #res {
              background: lightgray;
              border: solid;
              width: 81%;
              height: 48px;
              font-size: 20px;
              color: black;
              float: center;
            }
            #btns {
              width: 90%;
              text-align: center 
              width: 22%;
              height: 36px;
              font-size: 18px;
              float: center;
            }
            .upper {
              display: inline;
              position: top;
            }
            .lgreen {
              background: lightgreen;
              color: brown;
              display: inline;
              width: 22%;
              height: 36px;
              font-size: 18px;
            }
            .dgreen {
              background: darkgreen;
              color: white;
              display: inline;
              width: 22%;
              height: 36px;
              font-size: 18px;
            }
            .lower {
              disply: inline;
              position: bottom;
            }
            .operator {
              background: black;
              color: red;
              height: 36px;
              width: 22%;
              font-size 18px;
            }
        </style>
        <meta charset="utf-8">
        </head>
    <body>
        <div id="res"></div>
        <div id="btns">
            <div class="upper">
                <button class="lgreen" id="btn0" onclick="key('0')">0</button>
                <button class="lgreen" id="btn1" onclick="key('1')">1</button>
                <button class="dgreen" id="btnClr" onclick="cl()">C</button>
                <button class="dgreen" id="btnEql" onclick="operatorFunx()">=</button>
            </div>
              <div class="lower">
                <button id="btnSum" class="operator" onclick="key('+')">
                  +</button>
                <button id="btnSub" class="operator" onclick="key('-')">
                  -</button>
                <button id="btnMul" class="operator" onclick="key('*')">
                  *</button>
                <button id="btnDiv" class="operator" onclick="key('/')">
                  /</button>
              </div>
            </div>  
        <script>
            var screen="";
            function operatorFunx(){
                if(screen.indexOf("+")!= -1){
                    var numbers = screen.split("+");
                    var x = parseInt(numbers[0],2);
                    var y = parseInt(numbers[1],2);
                    var sum = x+y;
                    var ans = sum.toString(2);
                }
                else if(screen.indexOf("-")!= -1){
                    var numbers = screen.split("-");
                    var x = parseInt(numbers[0],2);
                    var y = parseInt(numbers[1],2);
                    var sub = x-y;
                    var ans = sub.toString(2);
                }
                else if(screen.indexOf("*")!= -1){
                    var numbers = screen.split("*");
                    var x = parseInt(numbers[0],2);
                    var y = parseInt(numbers[1],2);
                    var mul = x*y;
                    var ans = mul.toString(2);
                }
                else if(screen.indexOf("/")!= -1){
                    var numbers = screen.split("/");
                    var x = parseInt(numbers[0],2);
                    var y = parseInt(numbers[1],2);
                    var div = x/y;
                    var ans = div.toString(2);
                }
                screen = ans;
                document.getElementById("res").innerHTML = screen;
            }
            function key(c){
                console.log(screen);
                screen += c;
                document.getElementById("res").innerHTML = screen;
            }
            function cl(){
                screen="";
                document.getElementById("res").innerHTML=screen;
            }
                    
        </script>
    </body>
</html>