// Credit card number checker that uses Luhn algorithm to find out if a credit card number is valid or not. Samples are from the web, but any other, i.e your own credit card number
// could be check. PLEASE do not save your real credit card number anywhere on the web without any security of specific purpose.

// All valid credit card numbers
const valid1 = [4, 5, 3, 9, 6, 7, 7, 9, 0, 8, 0, 1, 6, 8, 0, 8];
const valid2 = [5, 5, 3, 5, 7, 6, 6, 7, 6, 8, 7, 5, 1, 4, 3, 9];
const valid3 = [3, 7, 1, 6, 1, 2, 0, 1, 9, 9, 8, 5, 2, 3, 6];
const valid4 = [6, 0, 1, 1, 1, 4, 4, 3, 4, 0, 6, 8, 2, 9, 0, 5];
const valid5 = [4, 5, 3, 9, 4, 0, 4, 9, 6, 7, 8, 6, 9, 6, 6, 6];

// All invalid credit card numbers
const invalid1 = [4, 5, 3, 2, 7, 7, 8, 7, 7, 1, 0, 9, 1, 7, 9, 5];
const invalid2 = [5, 7, 9, 5, 5, 9, 3, 3, 9, 2, 1, 3, 4, 6, 4, 3];
const invalid3 = [3, 7, 5, 7, 9, 6, 0, 8, 4, 4, 5, 9, 9, 1, 4];
const invalid4 = [6, 0, 1, 1, 1, 2, 7, 9, 6, 1, 7, 7, 7, 9, 3, 5];
const invalid5 = [5, 3, 8, 2, 0, 1, 9, 7, 7, 2, 8, 8, 3, 8, 5, 4];

// Can be either valid or invalid
const mystery1 = [3, 4, 4, 8, 0, 1, 9, 6, 8, 3, 0, 5, 4, 1, 4];
const mystery2 = [5, 4, 6, 6, 1, 0, 0, 8, 6, 1, 6, 2, 0, 2, 3, 9];
const mystery3 = [6, 0, 1, 1, 3, 7, 7, 0, 2, 0, 9, 6, 2, 6, 5, 6, 2, 0, 3];
const mystery4 = [4, 9, 2, 9, 8, 7, 7, 1, 6, 9, 2, 1, 7, 0, 9, 3];
const mystery5 = [4, 9, 1, 3, 5, 4, 0, 4, 6, 3, 0, 7, 2, 5, 2, 3];

// An array of all the arrays above
const batch = [valid1, valid2, valid3, valid4, valid5, invalid1, invalid2, invalid3, invalid4, invalid5, mystery1, mystery2, mystery3, mystery4, mystery5];



const validateCred = (arr) => {
  // Starting from the farthest digit to the right, AKA the check digit, iterate to the left
  let modified_arr = [];
  let total = 0;

  for (let i = arr.length - 1; i >= 0; i--) {
  // As you iterate to the left, every other digit is doubled (the check digit is not doubled).
    if ((arr.length - 1 - i) % 2 === 1){
      arr[i] *= 2;
  // If the number is greater than 9 after doubling, subtract 9 from its value.
      if (arr[i] > 9) {
        arr[i] -= 9
      }
    }
    modified_arr.push(arr[i]);
    }
  // Sum up all the digits in the credit card number.
  for (let i = 0; i < modified_arr.length; i++){
    total += modified_arr[i];
  }
  //If the sum modulo 10 is 0 (if the sum divided by 10 has a remainder of 0) then the number is valid, otherwise, it’s invalid.
  if (total % 10 === 0) {
    return "Credit card number is valid"
  } else {
    return "Credit card number is invalid"
  }
}

console.log(validateCred(valid1));
console.log(validateCred(invalid2));

// This function scans all credit cards in the array "batch" and return invalid numbers
const findInvalidCards = temp => {
  let invalid_cards = []
  for (let card = 0; card < batch.length; card++) {
    if (validateCred(batch[card]) === "Credit card number is invalid") {
      invalid_cards.push(batch[card])
    }
  }
  return invalid_cards;
}

console.log(findInvalidCards(batch))

// This piece of code allows to check which companies issued invalid credit card numbers:

/* First Digit	Company
        3	      Amex (American Express)
        4	      Visa
        5	      Mastercard
        6	      Discover
*/

const idInvalidCardCompanies = (temp) => {
    let invalid_companies = [];
    for (let card of batch) {
      if (card[0] != 3 && card[0] != 4 && card[0] != 5 && card[0] != 6) {
        console.log("Company not found");
      } else if (card[0] === 3) {
        invalid_companies.push("Amex (American Express): " + card.join(', '));
      } else if (card[0] === 4) {
        invalid_companies.push("Visa: " + card.join(', '));
      } else if (card[0] === 5) {
        invalid_companies.push("Mastercard: " + card.join(', '));
      } else if (card[0] === 6) {
        invalid_companies.push("Discover: " + card.join(', '));
      }
    }
    return invalid_companies;
  };
  
  console.log(idInvalidCardCompanies(findInvalidCards(batch)));






