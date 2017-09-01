public class LinkedListDeque<ItemType> {

    /** subclass to hide nakedness of DataStructure  */
    private class Node{
        public Node prev;
        public ItemType item;
        public Node next;

        public Node(Node p ,ItemType i, Node n){
            prev = p;
            item = i;
            next = n;
        }
    }

    /** members of LinkedListDeque used for obtain information */
    private int size;
    private Node sentinel;
    private Node first;

    public LinkedListDeque() {
        size = 0;
        sentinel = new Node(sentinel, null, sentinel);

    }

    /** checks if Linked List is Empty */
    public boolean isEmpty(){
        if (size < 1){
            return true;
        }
        return false;
    }

    /** returns the size of LinkedList */
    public int size(){
        return size;
    }

    /** adds an item to the linked list and previous and next instant variable never return to
     * Sentinel
     * SEE JAVA VISUALISER SITE BELLOW */
    //https://cscircles.cemc.uwaterloo.ca/java_visualize/#code=public+class+LinkedListDeque%3CItemType%3E+%7B%0A%0A++++/**+subclass+to+hide+nakedness+of+DataStructure++*/%0A++++private+class+Node%7B%0A++++++++public+Node+prev%3B%0A++++++++public+ItemType+item%3B%0A++++++++public+Node+next%3B%0A%0A++++++++public+Node(Node+p+,ItemType+i,+Node+n)%7B%0A++++++++++++prev+%3D+p%3B%0A++++++++++++item+%3D+i%3B%0A++++++++++++next+%3D+n%3B%0A++++++++%7D%0A++++%7D%0A%0A++++/**+members+of+LinkedListDeque+used+for+obtain+information+*/%0A++++private+int+size%3B%0A++++private+Node+sentinel%3B%0A++++private+Node+first%3B%0A%0A++++public+LinkedListDeque()+%7B%0A++++++++size+%3D+0%3B%0A++++++++sentinel+%3D+new+Node(sentinel,+null,+sentinel)%3B%0A%0A++++%7D%0A%0A++++/**+checks+if+Linked+List+is+Empty+*/%0A++++public+boolean+isEmpty()%7B%0A++++++++if+(size+%3C+1)%7B%0A++++++++++++return+true%3B%0A++++++++%7D%0A++++++++return+false%3B%0A++++%7D%0A%0A++++/**+returns+the+size+of+LinkedList+*/%0A++++public+int+size()%7B%0A++++++++return+size%3B%0A++++%7D%0A%0A++++/**+adds+an+item+to+the+linked+list+*/%0A++++public+void+addFirst(ItemType+x)+%7B%0A++++++++Node+newFrontNode%3B%0A++++++++//Node+pointer%3B%0A%0A++++++++if+(isEmpty())+%7B%0A%0A++++++++++++newFrontNode+%3D+new+Node(sentinel,+x,+sentinel)%3B%0A++++++++++++sentinel.next+%3D+newFrontNode%3B%0A++++++++++++sentinel.prev+%3D+newFrontNode%3B%0A++++++++++++sentinel.prev.prev+%3D+newFrontNode%3B%0A++++++++++++sentinel.next.next+%3D+newFrontNode%3B%0A++++++++++++size+%2B%3D1%3B%0A++++++++++++return%3B%0A%0A++++++++%7D+else+%7B%0A++++++++++++Node+oldFrontNode+%3D+sentinel.next%3B%0A++++++++++++newFrontNode+%3D+new+Node(oldFrontNode.prev,+x,+oldFrontNode)%3B%0A++++++++++++//pointer+%3D+oldFrontNode.prev%3B%0A++++++++++++//if+(size+%3C+2)+%7B%0A++++++++++++//++++sentinel.prev+%3D+newFrontNode.next%3B%0A++++++++++++//%7D%0A%0A++++++++%7D%0A++++++++sentinel.next+%3D+newFrontNode%3B%0A%0A++++++++//sentinel.next.prev+%3D+pointer%3B%0A++++++++sentinel.prev.next+%3D+newFrontNode%3B%0A++++++++//sentinel.prev.prev+%3D+pointer.next%3B%0A++++++++newFrontNode.next.prev+%3D+newFrontNode%3B%0A%0A%0A++++++++first+%3D+sentinel.next%3B%0A++++++++size+%2B%3D+1%3B%0A++++%7D%0A%0A%0A++++public+static+void+main(String%5B%5D+args)%7B%0A++++++++LinkedListDeque%3CInteger%3E+L+%3D+new+LinkedListDeque%3C%3E()%3B%0A++++++++L.addFirst(4)%3B%0A++++++++L.addFirst(3)%3B%0A++++++++L.addFirst(2)%3B%0A++++++++L.addFirst(1)%3B%0A++++++++L.addFirst(0)%3B%0A++++++++//System.out.println(L.first.item)%3B%0A++++++++//System.out.println(L.first.prev.item)%3B%0A++++++++//System.out.println(L.first.prev.next.item)%3B%0A++++%7D%0A%0A%0A%0A%0A%7D&mode=display&curInstr=137
    public void addFirst(ItemType x) {

        Node newFrontNode;

        if (isEmpty()) {
            // if Linked List is empty we create a new node whose previous and next item is itself.
            newFrontNode = new Node(sentinel, x, sentinel);
            sentinel.next = newFrontNode;
            sentinel.prev = newFrontNode;
            sentinel.prev.prev = newFrontNode;
            sentinel.next.next = newFrontNode;
            size +=1;
            return;

        } else {
            /* if Linked List is not empty we construct a NEW NODE whose:
                previous point to the last node.
                and whose next points to the beginning of the OLD NODE (in other words the new second node).
              */
            Node oldFrontNode = sentinel.next;
            newFrontNode = new Node(oldFrontNode.prev, x, oldFrontNode);

        }
        /* we then adjust the sentinel pointer to so that the pointers reflect the following changes:
            Next from sentinel points to the new front Node .
            Next from last node points to new front Node.
            previous from second Node points new front node.
         */
        sentinel.next = newFrontNode;
        sentinel.prev.next = newFrontNode;
        newFrontNode.next.prev = newFrontNode;


        first = sentinel.next;
        size += 1;
    }


    public void addLast(ItemType x){
        Node newLastNode;

        if(isEmpty()){
            newLastNode = new Node(sentinel, x, sentinel);
            sentinel.next = newLastNode;
            sentinel.prev = newLastNode;
            sentinel.prev.prev = newLastNode;
            sentinel.next.next = newLastNode;
            size +=1;
            return;
        }else{
            //Node newLastNode = sentinel.prev;
            Node oldFrontNode = sentinel.next;
            newLastNode = new Node(oldFrontNode.next, x, oldFrontNode.prev);

        }
        sentinel.prev = newLastNode;
        sentinel.next.prev = newLastNode;
        newLastNode.next.next = newLastNode;


        first = sentinel.next;
        size += 1;

    }

    public void printDeque(){
        int indx = 0;
        Node pointer = sentinel.next;
        while(indx!= size){
            System.out.print(pointer.item + " ");
            pointer = pointer.next;
            indx +=1;
        }
    }

    public ItemType get(int indx){
        int itter = 0;
        Node pointer = sentinel.next;
        while(itter != indx){
            pointer = pointer.next;
            itter +=1;
        }
        return pointer.item;

    }

    public void removeFirst(){
        if (size  <= 1){
            sentinel.next = sentinel;
            sentinel.prev = sentinel;
            first = sentinel;
            size = 0;
        } else {

        sentinel.next = sentinel.next.next;
        sentinel.next.prev = sentinel.next.next;
        sentinel.prev.next = sentinel.next;
        sentinel.next.prev = sentinel.next;
        first = sentinel.next;
        size -=1;
        }


    }

    public void removeLast(){
        if (size  <= 1){
            sentinel.next = sentinel;
            sentinel.prev = sentinel;
            first = sentinel;
            size = 0;
        } else {
            sentinel.prev = sentinel.prev.prev;
            sentinel.prev.next = sentinel.next;
            sentinel.next.prev = sentinel.prev;

            first = sentinel.next;
            size -= 1;
        }
    }

    public ItemType getRecursive(int index){

        if(index == 0){
            return first.item;
        }
        else {
            first = first.next;
            return getRecursive(index-1);
        }
    }

    public static void main(String[] args){
        LinkedListDeque<Integer> L = new LinkedListDeque<>();
        //L.addLast(1);
        //L.addLast(2);
        L.addLast(3);
        L.addFirst(0);
        L.removeFirst();
        L.removeLast();
        L.printDeque();

        //System.out.println(L.getRecursive(2));
        //System.out.println(L.get(2));

    }




}