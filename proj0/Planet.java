/** Project 0 Constructing a animated solar system. 
*/
public class Planet {

    /** xxPos, yyPos, xxVel ... are instance variable. they are called on by constructing a 
        new planet and using dot notation 

        Ex 1)
        planet p = new Planet();
        p.xxPos = 20;
        p.yyPos = 10;
              .
              .
              .
        System.out.print(p.xxPos);
    */
    Double xxPos, yyPos, xxVel, yyVel, mass;
    String imgFileName;
    // -----------------------------------------------------------------------------------
    /** This a a Planet Constructor it purpose is to save time and lines of code.
        Instead of constructing a planet instance and then assigning a value to each instance 
        variable, like in the above example, we do it all in one shot.

        Ex 2) 
        Planet p = new Planet(1,2,3,4,5,"nothing");
        System.out.println(p.xxPos);
        */

   public Planet(double xP, double yP, double xV, double yV, double m, String img){
       xxPos = xP;
       yyPos = yP;
       xxVel = xV;
       yyVel = yV;
       mass = m;
       imgFileName = img;
    }
    /**  Constructing a constructor that creates a copy of a planet instance.
    */
    public Planet(Planet p){
      xxPos = p.xxPos;
      yyPos = p.yyPos;
      xxVel = p.xxVel;
      yyVel = p.yyVel;
      mass  = p.mass;
      imgFileName = p.imgFileName;
    }

    /** Calculates the distance between two planets */
    public double calcDistance( Planet p2){
        return Math.sqrt(Math.pow(p2.xxPos - this.xxPos, 2) + Math.pow(p2.yyPos - this.yyPos,2));
    }

    /** Calculates the gravitational force between two planets. (F= gm1m2/r^2) */
    public double calcForceExertedBy(Planet p2){
        return (6.67e-11 * this.mass* p2.mass)/Math.pow(this.calcDistance(p2),2);
    }

    /** calculates the x component of the gravitational force using trigonometry (similar triangels).
        F*cos = F*(x2 - x1)/R , where R is the hypotenuse  */
    public double calcForceExertedByX(Planet p2) {
        return this.calcForceExertedBy(p2) * ((p2.xxPos - this.xxPos)/calcDistance(p2));
    }

    /** calculates the y component of the gravitational force using trigonometry (similar triangels).
     F*cos = F*(y2 - y1)/R , where R is the hypotenuse  */
    public double calcForceExertedByY(Planet p2) {
        return this.calcForceExertedBy(p2) * ((p2.yyPos - this.yyPos)/ this.calcDistance(p2));
    }

    /** sums up all forces in the x direction */
    public double calcNetForceExertedByX(Planet[] allplanets){
        double netForce = 0;

        for (Planet plaNet : allplanets){
            if (!this.equals(plaNet)){
                netForce = netForce + this.calcForceExertedByX(plaNet);
            }
        }
        return netForce;
    }

    /** sums up all forces in the y direction */
    public double calcNetForceExertedByY(Planet[] allplanets) {
        double netForce = 0;

        for (Planet plaNet : allplanets) {
            if (!this.equals(plaNet)) {
                netForce = netForce + this.calcForceExertedByY(plaNet);
            }
        }
        return netForce;
    }

    /** updates position of planets by calculating the acceleration in the
     *  x and y direction and applying kinematics to work out their new position.
     *  fX --> net force in x direction exerted on a test planet
     *  fY --> net force in Y direction exerted on a test planet
     *  dt --> change in time */
    public void update(double dt, double fX, double fY){
        double ax = fX / this.mass;
        double ay = fY / this.mass;
        this.xxVel = this.xxVel + ax * dt;
        this.yyVel = this.yyVel + ay * dt;
        this.xxPos = this.xxPos + this.xxVel * dt;
        this.yyPos = this.yyPos + this.yyVel * dt;
    }

    /** draws a planet in specified x and y positon*/
    public void draw(){
        StdDraw.picture(xxPos, yyPos, imgFileName);
        //StdDraw.show(2000);
    }
}
