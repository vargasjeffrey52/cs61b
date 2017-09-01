import java.awt.font.NumericShaper;
/** this class will run the Planet class */
public class NBody {

    /** home directory for images of planets and background stars*/
    public static String dirFile = "./images/";
    public static String starFieldBackground = "starfield.jpg";

    /** used to read the radius in the ./data/planet.txt file. Reads the lines */
    public static double readRadius(String fname ){
        In pathFile = new In(fname);
        int numPlanets = pathFile.readInt();
        double radius = pathFile.readDouble();
        return radius;
    }
    /**  reads lines in .txt file that contain planet info */
   public static Planet[] readPlanets(String fname){
       In pathFile = new In(fname);
       int numPlanets = pathFile.readInt();
       double radius = pathFile.readDouble();
       int dummyIndx = 0;
       Planet[] planets = new Planet[numPlanets];
       while (dummyIndx < numPlanets ){
           planets[dummyIndx] = new Planet(0.0, 0.0, 0.0, 0.0, 0.0, "");
           planets[dummyIndx].xxPos = pathFile.readDouble();
           planets[dummyIndx].yyPos = pathFile.readDouble();
           planets[dummyIndx].xxVel = pathFile.readDouble();
           planets[dummyIndx].yyVel = pathFile.readDouble();
           planets[dummyIndx].mass = pathFile.readDouble();
           planets[dummyIndx].imgFileName = pathFile.readString();
           dummyIndx +=1;
       }
       return planets;

   }

   /** used to make animation. of planets. */
   public static void main(String[] args){

       double T = Double.parseDouble(args[0]);
       double dt = Double.parseDouble(args[1]);
       String filename = args[2];

       Planet[] planets = readPlanets(filename);
       for (Planet p: planets) {
           p.imgFileName = dirFile + p.imgFileName;
       }

       double radius  = readRadius(filename);
       //StdDraw.setCanvasSize(1000,800);
       StdDraw.setScale(-radius,radius);

       double time = 0;
       double[] xForces = new double[planets.length];
       double[] yForces = new double[planets.length];

       while (time < T){
           planetLoop(planets);
           for (int indx  = 0;indx  < planets.length;indx++){
               xForces[indx] = planets[indx].calcNetForceExertedByX(planets);
               yForces[indx] = planets[indx].calcNetForceExertedByY(planets);
           }
           int indx = 0;
           for(Planet p : planets){
               p.update(dt, xForces[indx], yForces[indx]);
               indx +=1;
           }
           time += dt;
       }

   }

   /** used to loop over and draw each planet in planet array */
   public static void planetLoop(Planet[] planets){
        StdDraw.clear();
        StdDraw.picture(0, 0, dirFile+starFieldBackground);
        //StdDraw.picture(0, 0, dirFile+starFieldBackground,2.50e+11*2,2.50e+11*2);
        for (Planet p: planets){
            //p.imgFileName = dirFile + p.imgFileName;
            p.draw();
        }
        StdDraw.show(10);
    }
}
