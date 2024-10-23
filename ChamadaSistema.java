
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class ChamadaSistema {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        limparTela();
        System.out.print("> digite o nome do arquivo: ");
        String nomeArquivo = scanner.nextLine();

        File arquivo = new File(nomeArquivo);

        try {
            if (arquivo.createNewFile()) {
                System.out.println("\n> arquivo " + nomeArquivo + " criado com sucesso!");
            } else {
                System.out.println("\n> arquivo informado já existe!");
            }

            // escreve no arquivo
            FileWriter escritor = new FileWriter(arquivo);
            escritor.write("Só alegria hahaha");
            escritor.close();
            System.out.println("\n> texto adicionado ao arquivo!\n");
        } catch (IOException e) {
            System.out.println("\n ocorreu um erro ao criar o arquivo ...");
            e.printStackTrace();
        }

        scanner.close();
    }

    public static void limparTela() {
        try {
            if (System.getProperty("os.name").contains("Windows")) {
                // limpa tela no windows
                new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
            } else {
                // limpa tela no linux 
                new ProcessBuilder("clear").inheritIO().start().waitFor();
            }
        } catch (IOException | InterruptedException ex) {
            ex.printStackTrace();
        }
    }
}
