
function printValue() {
    var inputValue1 = document.getElementById("gre").value;
    var radio1 = document.getElementById("option1");
    var radio2 = document.getElementById("option2");
    var radio3 = document.getElementById("option3");
    var radio4 = document.getElementById("option4");
    var radio5 = document.getElementById("option5");

    if (inputValue1 >=0 && inputValue1 <=70){
        radio1.checked = true;
    }
    else if(inputValue1>=71 && inputValue1<=140){
        radio2.checked = true;
    }
    else if(inputValue1>=141 && inputValue1<=210){
        radio3.checked = true;
    }
    else if(inputValue1>=211 && inputValue1<=280){
        radio4.checked = true;
    }
    else if(inputValue1>=281 && inputValue1<=350){
        radio5.checked = true;
    }
    else{
        radio5.checked = true;
    }
}

function printOutput(){
    var inputValue1 = document.getElementById("cgpa").value;
    var radio1 = document.getElementById("research1");
    var radio2 = document.getElementById("research2");

    if (inputValue1 >=0 && inputValue1 <=4){
        radio2.checked = true;
    }
    else if(inputValue1>=4 && inputValue1<=10){
        radio1.checked = true;
    }
    else{
        radio1.checked = true;
    }

}