
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
                System.out.println("\n> arquivo '" + nomeArquivo + "' criado com sucesso!");
            } else {
                System.out.println("\n> arquivo informado já existe!");
            }

            exibirMenu(scanner, arquivo);

        } catch (IOException e) {
            System.out.println("\n> ocorreu um erro ao manipular o arquivo ...");
            e.printStackTrace();
        }

        scanner.close();
    }

    public static void exibirMenu(Scanner scanner, File arquivo) {
        String opcao = "";

        while (!opcao.equals("0")) {
            System.out.println("\n------------ menu ------------");
            System.out.println("1. editar conteúdo do arquivo");
            System.out.println("2. adicionar mensagem ao arquivo");
            System.out.println("0. sair");
            System.out.println("------------------------------");
            System.out.print("> opção: ");
            opcao = scanner.nextLine();

            switch (opcao) {
                case "1":
                    System.out.print("\n> digite a nova mensagem para editar o conteúdo do arquivo: ");
                    String novaMensagem = scanner.nextLine();
                    editarArquivo(arquivo, novaMensagem);
                    break;
                case "2":
                    System.out.print("\n> digite a mensagem para adicionar ao arquivo: ");
                    String mensagemAdicional = scanner.nextLine();
                    adicionarMensagemAoArquivo(arquivo, mensagemAdicional);
                    break;
                case "0":
                    limparTela();
                    System.out.println("\n> saindo...");
                    break;
                default:
                    limparTela();
                    System.out.println("\n> opção inválida!");
                    break;
            }
        }
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

    public static void editarArquivo(File arquivo, String novaMensagem) {
        try (FileWriter escritor = new FileWriter(arquivo)) {
            escritor.write(novaMensagem);
            System.out.println("\n> arquivo editado com sucesso!");
        } catch (IOException e) {
            System.out.println("\n> erro ao editar o arquivo ...");
            e.printStackTrace();
        }
    }

    public static void adicionarMensagemAoArquivo(File arquivo, String mensagem) {
        try (FileWriter escritor = new FileWriter(arquivo, true)) {
            escritor.write("\n" + mensagem);
            System.out.println("\n> mensagem adicionada ao arquivo com sucesso!");
        } catch (IOException e) {
            System.out.println("\n> erro ao adicionar ao arquivo ...");
            e.printStackTrace();
        }
    }
}
