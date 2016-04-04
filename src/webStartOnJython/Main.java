package webStartOnJython;

import webStartOnJython.interfaces.JySwingType;
import org.plyjy.factory.JythonObjectFactory;
// Uncomment this if you want to debug interpreter import errors
//import org.python.util.PythonInterpreter;


class Main {

    JythonObjectFactory factory;

    public static void invokeJython(String[] args) {
        /*
        // Uncomment if you want to debug import errors
        PythonInterpreter interpreter = new PythonInterpreter();

        interpreter.exec("from WebStartOnJythonImpl import WebStartOnJythonImpl");
        */

        JySwingType jySwing = (JySwingType) JythonObjectFactory
            .createObject(JySwingType.class, "WebStartOnJythonImpl");

        jySwing.start(args);
    }

    public static void main(String[] args) {
        System.out.println("Invoking Jython");
        invokeJython(args);
    }
}
