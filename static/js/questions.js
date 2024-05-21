let questionNo = parseInt(document.querySelector(".question_no").textContent);

let savefile = questionNo+ 'savekey'


function outf(text) {
  var mypre = document.getElementById("output");
  mypre.value = mypre.value + text;
}
function builtinRead(x) {
  if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
      throw "File not found: '" + x + "'";
  return Sk.builtinFiles["files"][x];
}

function run() {
  var t0 = (new Date()).getTime()
  var prog = editor.getValue();
  var mypre = document.getElementById("output");
  mypre.value = '';
  Sk.pre = "output";
  Sk.configure({
      inputfun: function (prompt) {
          return window.prompt(prompt);
      },
      inputfunTakesPrompt: true,
      output: outf,
      read: builtinRead,
      __future__: Sk.python3
  });
  var myPromise = Sk.misceval.asyncToPromise(function () {
      return Sk.importMainWithBody("<stdin>", false, prog, true);
  });
  myPromise.then(function () {
      var t1 = (new Date()).getTime()
      mypre.value = mypre.value + "\n" + "<completed in " + (t1 - t0) + " ms>";
  },
      function (err) {
          mypre.value = mypre.value + err.toString() + "\n";
          var t1 = (new Date()).getTime()
          mypre.value = mypre.value + "\n" + "<completed in " + (t1 - t0) + " ms>";
      });
};

function main() {
  run();
  var mypre = document.getElementById("output");
  mypre.style.display = 'block';
  editor.resize()
}
function outfr(text) {
  var mypre = document.getElementById("out");
  mypre.innerHTML = mypre.innerHTML + text;
}
function checkit(input) {
  var prog = editor.getValue();
  let codeli = prog.split("\n")
  for (i in codeli){
    if (codeli[i].includes('input')){
      codeli[i] = codeli[i].replaceAll(' ','')
      codeli[i] = codeli[i].replace('=input()', input[0])
    }
  }
  let code = codeli.join('\n')
  var mypre = document.getElementById("out");
  mypre.innerHTML = '';
  Sk.pre = "out";
  Sk.configure({output:outfr, read:builtinRead});
  (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = 'mycanvas';
  var myPromise = Sk.misceval.asyncToPromise(function() {
    return Sk.importMainWithBody("<stdin>", false, code, true);
  });
  // const finalOutput;
  myPromise.then(function(mod) {
      console.log('success');

    },
    function(err) {
      console.log(err.toString());
      // mypre.innerText = err.toString();
      // finalOutput=  err.toString();
    });
    return mypre.innerHTML
}
function checkAns(){
  let inputs ={q1_1: ['="hello"'],q1_2: ['="bye"'],q1_3: ['="4567"']}
  let ans = []
  if (questionNo == 1){
    for (let i=1; i <=3 ; i++){
      var ans1 = checkit(inputs['q1_'+i])
      ans.push(ans1)
  }}
  else if (questionNo == 2){
    for (let i=1; i <=3 ; i++){
      var ans1 = checkit(inputs['q1_'+i])
      ans.push(ans1)
  }}
  return ans
}

function checkAnswer(){
  let ans = checkAns()
  let correct = [['h\ne\nl\nl\no\n', 'b\ny\ne\n', '4\n5\n6\n7\n'],['olleh\n', 'eyb\n', '7654\n']]
  if (JSON.stringify(ans) == JSON.stringify(correct[questionNo-1])){
    return "Correct"}
  else{
    return "Incorrect"}



}

function sendResult() { 
  var value = checkAnswer(); 
  $.ajax({ 
      url: '/getResults', 
      type: 'POST', 
      contentType: 'application/json', 
      data: JSON.stringify({ 'value': value }), 
      success: function(response) { 
          console.log('Success Sent'); 
      }, 
      error: function(error) { 
          console.log(error); 
      } 
  }); 
} 
function openFile() {
  var files = input.files;
  if (files.length == 0) return;

  var file = files[0];
  var reader = new FileReader();
  reader.onload = (e) => {
      var file = e.target.result;
      var lines = file.split(/\r\n|\n/);
      editor.setValue(lines.join('\n'));
  };

  reader.onerror = (e) => alert(e.target.error.name);
  reader.readAsText(file);
};

function toggleConsole() {
  var mypre = document.getElementById("output");
  if (mypre.style.display !== 'none') {
      mypre.style.display = 'none';
  }
  else {
      mypre.style.display = 'block';
  }
  editor.resize()
}

function saveCode() {
  localStorage[savefile] = editor.getValue();
  window.alert("Code saved!")
}
function saveCodeSubmit() {
  localStorage[savefile] = editor.getValue();
  window.alert("Submit code!")
}

function downloadCode() {
  var prog = editor.getValue();
  var hiddenElement = document.createElement('a');
  hiddenElement.href = 'data:attachment/text,' + encodeURI(prog);
  hiddenElement.download = 'download.py'+questionNo ;
  if (confirm('Download Code?')) {
      hiddenElement.click();
  }
}

function shareCode() {
  var link = window.location.href.split('?')[0] + "?code=" + encodeURIComponent(editor.getValue());
  window.prompt("Copy link to clipboard: Ctrl+C, Enter", link);
}

function kbShortcuts() {
  window.alert("Run : Ctrl+Enter\nOpen : Ctrl+Shift+O\nConsole : Ctrl+Shift+E\nSave : Ctrl+Shift+S\nDownload : Ctrl+Shift+D\nShare : Ctrl+Shift+A\nKeyboard : Ctrl+Shift+K")
}

function aceSettings() {
  editor.execCommand("showSettingsMenu")
}

function resPanel() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
      x.className += " responsive";
  } else {
      x.className = "topnav";
  }
}

document.addEventListener('keydown', (event) => {
  if (event.ctrlKey && event.key == "Enter") {
      event.preventDefault();
      main();
  }

  if (event.ctrlKey && event.shiftKey && event.key == "O") {
      event.preventDefault();
      input.click()
  }

  if (event.ctrlKey && event.shiftKey && event.key == "E") {
      event.preventDefault();
      toggleConsole();
  }

  if (event.ctrlKey && event.shiftKey && event.key == "S") {
      event.preventDefault();
      saveCode();
  }

  if (event.ctrlKey && event.shiftKey && event.key == "D") {
      event.preventDefault();
      downloadCode();
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
let def_code = "#Dont edit this line of code\n"
if (questionNo==4) {
    editor.setValue(def_code + "input_data = eval(input())");
  }
editor.session.setMode("ace/mode/python");
editor.setShowPrintMargin(false);
editor.commands.removeCommand('findprevious');
editor.commands.removeCommand('duplicateSelection');
editor.commands.removeCommand('replaymacro');
ace.require("ace/ext/language_tools");
editor.setOptions({
  fontFamily: "Consolas, 'Courier New', monospace",
  fontSize: "16x",
  enableBasicAutocompletion: true,
  enableSnippets: true,
  enableLiveAutocompletion: true,
  autoScrollEditorIntoView: true,

});

var savedCode = localStorage[savefile] || 'defaultValue';

if (savedCode != "defaultValue") {
  editor.setValue(savedCode);
}

var params = new Proxy(new URLSearchParams(window.location.search), {
  get: (searchParams, prop) => searchParams.get(prop),
});

if (params.code != null) {
  editor.setValue(params.code);
};

var input = document.querySelector('input')
input.addEventListener('change', () => {
  openFile();
});

window.addEventListener('beforeunload', function (event) {
  return null;
});

toggleConsole();