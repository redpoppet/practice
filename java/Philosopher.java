import java.util.Random;
import java.util.concurrent.locks.ReentrantLock;

public class Philosopher  extends Thread{

    private boolean eating;
    private Philosopher left;
    private Philosopher right;
    private ReentrantLock table;
    private Condition condition;
    private Random random;
    public Philosopher(ReentrantLock table){
        eating = false;
        this.table  = table;
        condition = table.newCondition();
        random = new Random()
    }
}