var Game = function() {
  	this.score = 0;
    this.rolls = [];

    this.roll = function(n) {
        this.rolls.push(n);
    }

    this.getScore = function() {
        if(this.score !== 0) {
            this.score = 0;
        }

        var midFrame = false;
        var isStrike = false;

        for(i = 0; i < this.rolls.length; i++) {
            if(this.rolls[i] === 10 || midFrame) {
                if(isStrike) {
                    if(midFrame) {
                            this.score += this.rolls[i] + this.rolls[i - 1];
                    } else {
                        if(i != this.rolls.length - 1) {
                            this.score += this.rolls[i] + this.rolls[i + 1];
                        }
                    }
                    isStrike = false;
                }

                if(this.rolls[i] === 10 && !midFrame) {
                    this.score += this.rolls[i];
                    isStrike = true;
                } else {
                    if((this.rolls[i-1] + this.rolls[i] === 10) && midFrame){
                        if(i != this.rolls.length - 1) {
                            this.score += this.rolls[i + 1];
                        }
                    }
                    this.score += this.rolls[i] + this.rolls[i-1];
                    if (midFrame) {
                        midFrame = false;
                    }
                }
            } else {
                    midFrame = true;
            }
        }

        return this.score;
    }
}

module.exports = Game;