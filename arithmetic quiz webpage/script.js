let num1, num2, operation, correctCount = 0, incorrectCount = 0;

function performOperation(op) {
    num1 = parseFloat(document.getElementById('num1').value);
    num2 = parseFloat(document.getElementById('num2').value);
    operation = op;
}

function checkAnswer() {
    const userAnswer = parseFloat(document.getElementById('userAnswer').value);
    let result;
    
    switch (operation) {
        case 'add':
            result = num1 + num2;
            break;
        case 'subtract':
            result = num1 - num2;
            break;
        case 'multiply':
            result = num1 * num2;
            break;
        case 'divide':
            result = num1 / num2;
            break;
    }

    const correct = result === userAnswer;

    if (correct) {
        correctCount++;
    } else {
        incorrectCount++;
    }

    const total = correctCount + incorrectCount;
    const percentage = ((correctCount / total) * 100).toFixed(2);

    document.getElementById('correctCount').textContent = correctCount;
    document.getElementById('incorrectCount').textContent = incorrectCount;
    document.getElementById('percentage').textContent = percentage + '%';

    alert(correct ? 'Correct!' : 'Incorrect! The correct answer is ' + result);
}
