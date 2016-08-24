import static org.junit.Assert.assertEquals;
import org.junit.*;

public class BowlingTest {
  private Bowling bowling;

  public void rollMany(Bowling game, int n, int pins) {
    for(int i = 0; i < n; i++) {
        game.roll(pins);
    }
  }

  @Before
  public void setUp() {
    this.bowling = new Bowling();
  }

  @Test
  public void gutterGame() {
    rollMany(this.bowling, 20, 0);

    assertEquals(this.bowling.getScore(), 0);
  }

  @Test
  public void allOnes() {
    rollMany(this.bowling, 20, 1);

    assertEquals(this.bowling.getScore(), 20);
  }

  @Test
  public void oneSpare() {
    this.bowling.roll(5);
    this.bowling.roll(5);
    this.bowling.roll(3);
    rollMany(this.bowling, 17, 0);

    assertEquals(this.bowling.getScore(), 16);
  }

  @Test
  public void falseSpare() {
    // if the scores that total to 10 are not in the same frame, it is not a spare.
    this.bowling.roll(0);
    this.bowling.roll(5);
    this.bowling.roll(5);
    this.bowling.roll(3);
    rollMany(this.bowling, 16, 0);

    assertEquals(this.bowling.getScore(), 13);
  }

  @Test
  public void oneStrike() {
    this.bowling.roll(10);
    this.bowling.roll(3);
    this.bowling.roll(4);
    rollMany(this.bowling, 16, 0);

    assertEquals(this.bowling.getScore(), 24);
  }

  @Test
  public void gutterAndTenMeansSpare() {
    this.bowling.roll(0);
    this.bowling.roll(10);
    this.bowling.roll(3);
    this.bowling.roll(4);
    rollMany(this.bowling, 16, 0);

    assertEquals(this.bowling.getScore(), 20);
  }

  @Test
  public void strikeFollowedBySpare() {
    this.bowling.roll(10);
    this.bowling.roll(3);
    this.bowling.roll(7);
    this.bowling.roll(4);
    this.bowling.roll(4);
    rollMany(this.bowling, 14, 0);

    assertEquals(this.bowling.getScore(), 42);
  }

  @Test
  public void strikeFollowedByStrike() {
    this.bowling.roll(10);
    this.bowling.roll(10);
    this.bowling.roll(3);
    this.bowling.roll(4);
    rollMany(this.bowling, 14, 0);

    assertEquals(this.bowling.getScore(), 47);
  }

  @Test
  public void spareFollowedBySpare() {
    this.bowling.roll(3);
    this.bowling.roll(7);
    this.bowling.roll(10);
    this.bowling.roll(3);
    this.bowling.roll(4);
    rollMany(this.bowling, 14, 0);

    assertEquals(this.bowling.getScore(), 44);
  }

  @Test
  public void spareFollowedByStrike() {
    this.bowling.roll(3);
    this.bowling.roll(7);
    this.bowling.roll(10);
    this.bowling.roll(3);
    this.bowling.roll(4);
    rollMany(this.bowling, 14, 0);

    assertEquals(this.bowling.getScore(), 44);
  }

  @Test
  public void lasFrameNormalCase() {
    rollMany(this.bowling, 18, 0);
    this.bowling.roll(3);
    this.bowling.roll(4);

    assertEquals(this.bowling.getScore(), 7);
  }

  @Test
  public void lastFrameSpare() {
    rollMany(this.bowling, 18, 0);
    this.bowling.roll(3);
    this.bowling.roll(7);
    this.bowling.roll(9);

    assertEquals(this.bowling.getScore(), 19);
  }

  @Test
  @Ignore
  public void lastFrameStrike() {
    rollMany(this.bowling, 18, 0);
    this.bowling.roll(10);
    this.bowling.roll(3);
    this.bowling.roll(4);

    assertEquals(this.bowling.getScore(), 17);
  }

  @Test
  @Ignore
  public void lastFrameStrikeFollowedByspare() {
    rollMany(this.bowling, 18, 0);
    this.bowling.roll(10);
    this.bowling.roll(3);
    this.bowling.roll(7);

    assertEquals(this.bowling.getScore(), 20);
  }

  @Test
  @Ignore
  public void perfectGame() {
    rollMany(this.bowling, 12, 10);

    assertEquals(this.bowling.getScore(), 300);
  }
}
