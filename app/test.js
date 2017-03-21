(function () {
  'use strict';

  describe("Expected number of divisors", function() {
    describe("Produces the correct output", function() {
      it("where A = 4 B = 38 and K = 3", function() {
        expect(evaluateDivisors(4,38,3)).toBe(3);
      });

      it("where A = 2 B = 55 and K = 5", function() {
        expect(evaluateDivisors(2,55,5)).toBe(1);
      });

      it("where A = 42 B = 250 and K = 9", function() {
        expect(evaluateDivisors(42,264,9)).toBe(4);
      });

      it("where A = 114 B = 503 and K = 15", function() {
        expect(evaluateDivisors(114,503,15)).toBe(3);
      });

    });
    describe("Handles larger ranges,", function() {
      it("Handles a range of 25k where A = 1103 B = 51103 and K = 17", function() {
        expect(evaluateDivisors(1103,26103,21)).toBe(8);
      });

      //only un-x this spec if the specs suite is running in less than a second
      it("Handles a range of 1 billion where A = 1232 B = 1000001232 and K = 17", function() {
        expect(evaluateDivisors(1232,1000001232,9)).toBe(7807);
      });

      //  only un-x this if the specs suite including the 1 billion range is is running in less than 2 seconds
      it("Handles a range of 10 billion where A = 2543 B = 10000002543 and K = 5", function() {
        expect(evaluateDivisors(2543, 10000002543, 5)).toBe(61);
      });
    });
  });
})();
