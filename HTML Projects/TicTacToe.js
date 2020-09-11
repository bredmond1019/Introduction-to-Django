// Restart Game Button
var restart = document.querySelector('#b')


// Grab all the squares
var squares = document.querySelectorAll('td')

// Clear all the squares
function clearBoard(){
    for (var i = 0; i < squares.length; i++){
        squares[i].textContent = '';
    }
}

restart.addEventListener('click', clearBoard);

// Check the square marker
function changeMarker(){
    if (this.textContent === ""){
        this.textContent = 'X';
    }
    else if (this.textContent === 'X'){
        this.textContent = 'O'
    }
    else {
        this.textContent = ''
    }
}



// For loop to add event listeners to all the squares

for (let index = 0; index < squares.length; index++) {
    squares[index].addEventListener('click', changeMarker)
    
}













var xAndO = document.querySelector('#one')





xAndO.addEventListener("click", function () {
    if (xAndO.textContent == 'X') {
        xAndO.textContent = "O";
        xAndO.style.color = 'blue';
    }
    else if (xAndO.textContent == "O") {
        xAndO.textContent = ""
        
    }
    else{
        xAndO.textContent = "X"
    }
    
    
})



