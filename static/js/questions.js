let questionNo = parseInt(document.querySelector(".question_no").textContent);

let savefile = questionNo + "savekey";

function outf(text) {
  var mypre = document.getElementById("output");
  mypre.value = mypre.value + text;
}
function builtinRead(x) {
  if (
    Sk.builtinFiles === undefined ||
    Sk.builtinFiles["files"][x] === undefined
  )
    throw "File not found: '" + x + "'";
  return Sk.builtinFiles["files"][x];
}

function run() {
  var t0 = new Date().getTime();
  var prog = editor.getValue();
  var mypre = document.getElementById("output");
  mypre.value = "";
  Sk.pre = "output";
  Sk.configure({
    inputfun: function (prompt) {
      return window.prompt(prompt);
    },
    inputfunTakesPrompt: true,
    output: outf,
    read: builtinRead,
    __future__: Sk.python3,
  });
  var myPromise = Sk.misceval.asyncToPromise(function () {
    return Sk.importMainWithBody("<stdin>", false, prog, true);
  });
  myPromise.then(
    function () {
      var t1 = new Date().getTime();
      mypre.value = mypre.value + "\n" + "<completed in " + (t1 - t0) + " ms>";
    },
    function (err) {
      mypre.value = mypre.value + err.toString() + "\n";
      var t1 = new Date().getTime();
      mypre.value = mypre.value + "\n" + "<completed in " + (t1 - t0) + " ms>";
    }
  );
}

function main() {
  run();
  let fullscrBtn = document.querySelector(".fullscr");
  fullscrBtn.innerHTML = "Full Screen";
  var mypre = document.getElementById("output");
  mypre.style.display = "block";
  editor.resize();
}
function outfr(text) {
  var mypre = document.getElementById("out");
  mypre.innerHTML = mypre.innerHTML + text;
}
function checkit(input) {
  prog = editor.getValue();
  let codeli = prog.split();
  function matchInputCalls(prog) {
    const pattern = /input\s*\(/g;
    const results = [];
    let match;

    while ((match = pattern.exec(prog)) !== null) {
      let start = match.index;
      let openParens = 1;
      let i = start + match[0].length;

      while (i < prog.length && openParens > 0) {
        if (prog[i] === "(") {
          openParens++;
        } else if (prog[i] === ")") {
          openParens--;
        }
        i++;
      }

      if (openParens === 0) {
        results.push(prog.slice(start, i));
      } else {
        console.log(
          "Unbalanced parentheses in input call starting at index " + start
        );
      }
    }

    return results;
  }

  const matches = matchInputCalls(prog);
  for (i in codeli) {
    for (j in matches) {
      if (codeli[i].includes("eval(" + matches[j] + ")")) {
        codeli[i] = codeli[i]
          .trim()
          .replace("eval(" + matches[j] + ")", input[j]);
      } else if (codeli[i].includes(matches[j])) {
        codeli[i] = codeli[i].trim().replace(matches[j], input[j]);
      }
    }
  }
  // console.log(matches)
  let code = codeli.join("/n");
  console.log(code);
  var mypre = document.getElementById("out");
  mypre.innerHTML = "";
  Sk.pre = "out";
  Sk.configure({ output: outfr, read: builtinRead });
  (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = "mycanvas";
  var myPromise = Sk.misceval.asyncToPromise(function () {
    return Sk.importMainWithBody("<stdin>", false, code, true);
  });
  // const finalOutput;
  myPromise.then(
    function (mod) {
      // console.log('success');
    },
    function (err) {
      mypre.innerHTML = mypre.innerHTML + err.toString() + "\n";
    }
  );
  // console.log(Error());
  return mypre.innerHTML;
}
function checkAns() {
  let inputs = {
    q1_1: ['"()(()"'],
    q1_2: ['"(()))())("'],
    q1_3: ['"(()()"'],
    q2_1: ['"ABBC"'],
    q2_2: ['"java"'],
    q2_3: ['"lol"'],
    q3_1: ["[1,2,3]"],
    q3_2: ["[1,2,3,4]"],
    q3_3: ["[3,4]"],
    q4_1: ["1"],
    q4_2: ["44"],
    q4_3: ["1994"],
    q5_1: ["3"],
    q5_2: ["11"],
    q5_3: ["15"],
    q6_1: ["'aa'", "'a*'"],
    q6_2: ["'mississippi'", "'m*issip*'"],
    q6_3: ["'abacb'", "'a*ba*b'"],
    q7_1: ["[[5,-3,3],[10,3,-5],[-20,3,-4]]", "[[-10],[27],[-4]]"],
    q7_2: ["[[1,-2,1],[2,1,1],[3,4,3]]", "[[3],[4],[-1]]"],
    q7_3: ["[[3, 0, -4],[0,3,2],[2,3,0]]", "[[0],[-3],[-5]]"],
    q8_1: ["3", "1"],
    q8_2: ["4", "16"],
    q8_3: ["5", "120"],
    q9_1: ['"aab"', '"xxy"'],
    q9_2: ["'aab'", "'xyz'"],
    q9_3: ["'ABACB'", "'XPZ'"],
    q10_1: ["'nnnnei'"],
    q10_2: ["'owoztneoerowoztneoer'"],
    q10_3: ["'fviefrurofuro'"],
  };
  let ans = [];
  if (questionNo == 1) {
    for (let i = 1; i <= 3; i++) {
      var ans1 = checkit(inputs["q1_" + i]);
      ans.push(ans1);
    }
  } else if (questionNo == 2) {
    for (let i = 1; i <= 3; i++) {
      var ans1 = checkit(inputs["q2_" + i]);
      ans.push(ans1);
    }
  } else if (questionNo == 3) {
    for (let i = 1; i <= 3; i++) {
      var ans1 = checkit(inputs["q3_" + i]);
      ans.push(ans1);
    }
  } else if (questionNo == 4) {
    for (let i = 1; i <= 3; i++) {
      var ans1 = checkit(inputs["q4_" + i]);
      ans.push(ans1);
    }
  } else if (questionNo == 5) {
    for (let i = 1; i <= 3; i++) {
      var ans1 = checkit(inputs["q5_" + i]);
      ans.push(ans1);
    }
  } else if (questionNo == 6) {
    for (let i = 1; i <= 3; i++) {
      var ans1 = checkit(inputs["q6_" + i]);
      ans.push(ans1);
    }
  } else if (questionNo == 7) {
    for (let i = 1; i <= 3; i++) {
      var ans1 = checkit(inputs["q7_" + i]);
      ans.push(ans1);
    }
  } else if (questionNo == 8) {
    for (let i = 1; i <= 3; i++) {
      var ans1 = checkit(inputs["q8_" + i]);
      ans.push(ans1);
    }
  } else if (questionNo == 9) {
    for (let i = 1; i <= 3; i++) {
      var ans1 = checkit(inputs["q9_" + i]);
      ans.push(ans1);
    }
  } else if (questionNo == 10) {
    for (let i = 1; i <= 3; i++) {
      var ans1 = checkit(inputs["q10_" + i]);
      ans.push(ans1);
    }
  }
  return ans;
}

function checkAnswer() {
  let ans = checkAns();
  let correct = [
    ["2\n", "4\n", "4\n"],
    ["CBBABBC\n", "avajava\n", "lol\n"],
    [
      "[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]\n",
      "[[1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2], [2, 1, 3, 4], [2, 1, 4, 3], [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 1, 3], [2, 4, 3, 1], [3, 1, 2, 4], [3, 1, 4, 2], [3, 2, 1, 4], [3, 2, 4, 1], [3, 4, 1, 2], [3, 4, 2, 1], [4, 1, 2, 3], [4, 1, 3, 2], [4, 2, 1, 3], [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1]]\n",
      "[[3, 4], [4, 3]]\n",
    ],
    ["I\n", "XLIV\n", "MCMXCIV\n"],
    ["3\n", "0\n", "2\n"],
    ["True\n", "False\n", "False\n"],
    ["[[1], [4], [-1]]\n", "[[4], [-1], [-3]]\n", "[[-4], [1], [-3]]\n"],
    ["123\n", "3241\n", "54321\n"],
    ["True\n", "False\n", "True\n"],
    ["9\n", "001122\n", "445\n"],
  ];
  console.log(ans);
  if (JSON.stringify(ans) === JSON.stringify(correct[questionNo - 1])) {
    return "Correct";
  } else {
    return "Incorrect";
  }
}
function saveCodeSubmit() {
  localStorage[savefile] = editor.getValue();
  window.alert("Submit code!");
}
function sendResult() {
  // console.log("working")s
  var value = checkAnswer();
  var userCode = editor.getValue();
  console.log(value);
  var csrftoken = "{{ csrf_token }}";
  const requestObj = new XMLHttpRequest();
  requestObj.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      window.location.href = "/questions/";
    }
  };
  requestObj.open("POST", "/post_correct/", true);
  requestObj.setRequestHeader("X-CSRFToken", csrftoken);
  formData = new FormData();
  formData.append("result", value);
  formData.append("qno", questionNo);
  formData.append("code", userCode);
  requestObj.send(formData);
  saveCodeSubmit();
}

function toggleConsole() {
  var mypre = document.getElementById("output");
  if (mypre.style.display !== "none") {
    mypre.style.display = "none";
  } else {
    mypre.style.display = "block";
  }
  editor.resize();
}

function saveCode() {
  localStorage[savefile] = editor.getValue();
  window.alert("Code saved!");
}

function shareCode() {
  var link =
    window.location.href.split("?")[0] +
    "?code=" +
    encodeURIComponent(editor.getValue());
  window.prompt("Copy link to clipboard: Ctrl+C, Enter", link);
}

function kbShortcuts() {
  window.alert(
    "Run : Ctrl+Enter\nOpen : Ctrl+Shift+O\nConsole : Ctrl+Shift+E\nSave : Ctrl+Shift+S\nDownload : Ctrl+Shift+D\nShare : Ctrl+Shift+A\nKeyboard : Ctrl+Shift+K"
  );
}

function aceSettings() {
  editor.execCommand("showSettingsMenu");
}

function resPanel() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}

document.addEventListener("keydown", (event) => {
  if (event.ctrlKey && event.key == "Enter") {
    event.preventDefault();
    main();
  }

  if (event.ctrlKey && event.shiftKey && event.key == "O") {
    event.preventDefault();
    input.click();
  }

  if (event.ctrlKey && event.shiftKey && event.key == "E") {
    event.preventDefault();
    toggleConsole();
  }

  if (event.ctrlKey && event.shiftKey && event.key == "S") {
    event.preventDefault();
    saveCode();
  }

  if (event.ctrlKey && event.shiftKey && event.key == "A") {
    event.preventDefault();
    shareCode();
  }

  if (event.ctrlKey && event.shiftKey && event.key == "K") {
    event.preventDefault();
    kbShortcuts();
  }
});

var editor = ace.edit("editor");
editor.setTheme("ace/theme/one_dark");
let def_code = "#Dont edit this line of code\n";
if (questionNo == 4) {
  editor.setValue(def_code + "input_data = eval(input())");
}
editor.session.setMode("ace/mode/python");
editor.session.setUseWrapMode(true);

editor.setShowPrintMargin(false);
editor.commands.removeCommand("findprevious");
editor.commands.removeCommand("duplicateSelection");
editor.commands.removeCommand("replaymacro");
ace.require("ace/ext/language_tools");
editor.setOptions({
  fontFamily: "Consolas, 'Courier New', monospace",
  fontSize: "16x",
  enableBasicAutocompletion: true,
  enableSnippets: true,
  enableLiveAutocompletion: true,
  autoScrollEditorIntoView: true,
});

var savedCode = localStorage[savefile] || "defaultValue";

if (savedCode != "defaultValue") {
  editor.setValue(savedCode);
}

var params = new Proxy(new URLSearchParams(window.location.search), {
  get: (searchParams, prop) => searchParams.get(prop),
});

if (params.code != null) {
  editor.setValue(params.code);
}

toggleConsole();

let editorDiv = document.querySelector(".editor-container");
let fullscreen = false;
function toggleFullScreen() {
  let shortcutBtn = document.querySelector(".shortcut");
  let questionDiv = document.querySelector(".questionDiv");
  let fullscrBtn = document.querySelector(".fullscr");
  let editorDiv = document.querySelector(".editor-container");
  if (fullscreen) {
    questionDiv.style.display = "block";
    editorDiv.style.display = "flex";
    editorDiv.style.width = "50%";
    editorDiv.style.height = "80vh";
    console.log("working");
    shortcutBtn.style.display = "none";
    fullscreen = false;
    fullscrBtn.innerHTML = "Full Screen";
    editor.session.setUseWrapMode(false);
    editor.session.setUseWrapMode(true);
  } else {
    questionDiv.style.display = "none";
    editorDiv.style.display = "block";
    editorDiv.style.width = "100%";
    editorDiv.style.height = "100vh";
    shortcutBtn.style.display = "inline-block";
    fullscreen = true;
    editor.session.setUseWrapMode(false);
    editor.session.setUseWrapMode(true);
    fullscrBtn.innerHTML = "Exit Full Screen";
  }
  console.log(fullscreen);
}
