//Practice using classes, inheritence, getters, setters and methods.


class Media {
    constructor(title, isCheckedOut = false, ratings = []) {
      this._title = title;
      this._isCheckedOut = isCheckedOut;
      this._ratings = ratings;
    }
      get title() {
        return this._title;
      }
  
      get isCheckedOut() {
        return this._isCheckedOut
      }
  
      get rating() {
        return this._ratings
      }
  
      toggleCheckOutStatus() {
        this._isCheckedOut = !this._isCheckedOut;
      }
  
      getAverageRating() {
        const ratingsSum = this._ratings.reduce((currentSum, rating) => currentSum + rating, 0);
        return ratingsSum / this._ratings.length
      }
  
      addRating(rating) {
        this._ratings.push(rating)
      }
    }
  
  class Book extends Media {
    constructor(author, title, pages) {
      super(title)
      this._author = author;
      this._pages = pages;
    }
  
    get author() {
      return this._author = author
    }
  
    get pages() {
      return this._pages = pages
    }
  }
  
  class Movie extends Media {
    constructor(director, title, runTime) {
      super(title)
      this._director = director;
      this._runTime = runTime; 
    }
  
    get director() {
      return this._director = director
    }
  
    get runTime() {
      return this._runTime = runTime
    }
  }

  // Testing the classes
  
  const historyOfEverything = new Book("Bill Bryson", 'A Short History of Nearly Everything', 544);
  
  historyOfEverything.toggleCheckOutStatus()
  historyOfEverything.isCheckedOut
  historyOfEverything.addRating(4);
  historyOfEverything.addRating(5);
  historyOfEverything.addRating(5);
  console.log(historyOfEverything.getAverageRating())
  
  const speed = new Movie("Jan de Bont", "Speed", 116)
  speed.toggleCheckOutStatus()
  speed.isCheckedOut
  speed.addRating(1)
  speed.addRating(1)
  speed.addRating(5)
  console.log(speed.getAverageRating())