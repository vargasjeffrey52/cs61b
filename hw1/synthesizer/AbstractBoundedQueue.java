package synthesizer;

public abstract class AbstractBoundedQueue<T> implements BoundedQueue<T> {


    protected int fillCount;
    protected int capacity;

    /** returns the capacity of the Queue */
    @Override
    public int capacity() {
        return this.capacity;
    }

    /** returns the Queue fillcount  */
    @Override
    public int fillCount() {
        return this.fillCount;
    }
}
