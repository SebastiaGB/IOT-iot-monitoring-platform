package Iotib.decoder;

public class Decoder {

    public static void main(String[] args) throws Exception {

        String baseUrl = System.getenv().getOrDefault("GATEWAY_BASE_URL", "<GATEWAY_BASE_URL>");
        Gateway_prueba conexionAPI = new Gateway_prueba(baseUrl);

        String gatewayUsername = System.getenv().getOrDefault("GATEWAY_USERNAME", "<GATEWAY_USERNAME>");
        String gatewayPassword = System.getenv().getOrDefault("GATEWAY_PASSWORD", "<GATEWAY_PASSWORD>");
        String token = conexionAPI.obtainToken(gatewayUsername, gatewayPassword);

        System.out.println("Token obtenido correctamente");

        conexionAPI.paquetesPorCampos(token);   
    }

}
