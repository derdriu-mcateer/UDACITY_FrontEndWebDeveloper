// Select color input
// Select size input
const color = document.getElementById("colorPicker");
const gridSize = document.getElementById("sizePicker");
const table = document.getElementById("pixelCanvas");
const submitButtom = document.getElementById("submit");


gridSize.addEventListener('submit', function (e) {
    //delete previous grid if any
    if (table.firstElementChild) {
        table.firstElementChild.remove();
    }
    // prevent grid disappearing
    e.preventDefault();
    // select grid size from h & w input values
    let height = document.getElementById('inputHeight').value;
    let width = document.getElementById('inputWidth').value;
    // When size is submitted by the user, call makeGrid()
    makeGrid(height, width);
})

function makeGrid(height, width) {
    // Your code goes here!

    // draws grid
    for (let y = 0; y < height; y++) {
        let row = table.insertRow(y);
        for (let x = 0; x < width; x++) {
            let cell = row.insertCell(x);
            // add event listerners to add color when clicked
            // & remove color if double clicked
            cell.addEventListener("click", function (e) {
                cell.style.backgroundColor = color.value;
                cell.addEventListener("dblclick", function (e) {
                    cell.style.backgroundColor = "rgb(61, 61, 61)";
                })
            })
        }
    }
}
