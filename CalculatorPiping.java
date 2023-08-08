import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class CalculatorPiping implements ActionListener {

    JFrame frame; //프로그램 화면
    JTextArea textArea; //입력값이나 결과괖이 나타나는 창
    JButton[] numberButtons = new JButton[10]; //숫자 버튼, 0부터 9까지 10가지
    JButton[] functionButtons = new JButton[14]; // +,-,*,/, decimal, =, del, all clear, negative 등 9가지 기호
    JButton addButton, subButton, mulButton, divButton; // 가감승제의 4가지 버튼
    JButton decButton, equButton, delButton, clrButton, negButton; //decimal, =, del, clear, negative 등 보조 연산자
    JButton elbButton, teeButton, redButton, othButton;
    JPanel panel; //0~9, 가감승제 버튼을 한번에 넣는 패널

    Font baseFont = new Font("Arial", Font.BOLD, 30); //글씨 크기 및 폰트
    Font fittingFont = new Font("Arial", Font.BOLD, 15);

    double num1=0, num2=0, result=0; //연산자를 기준으로 연산 대상이 되는 숫자값들이 입력되는 변수 2개
    char operator; //연산자를 가리키는 변수
    boolean startNewNo = false; //flag : num1 입력하고 연산자 입력시 숫자가 사라지지 않고, nmu2를 입력할 떄부터 숫자가 사라짐.


    CalculatorPiping(){
//----------------------프로그램 화면 세팅----------------//
        frame = new JFrame("Calculator");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(420,750); //윈도우 크기 설정
        frame.setLayout(null);
//----------------텍스트 입력 및 결과 입력 창 세팅------------//
        textArea = new JTextArea();
        textArea.setBounds(50, 25, 300, 100);
        textArea.setFont(baseFont);
        textArea.setEditable(false);
        textArea.setLineWrap(true); //디스플레이 창의 줄바꿈을 해 주는 코드
        textArea.setWrapStyleWord(true); //디스플레이 창의 틀 밖으로 글자가 벗어나지 않게 해 주는 코드
//---------9개의 연산 객체 생성-----------------------------//
        addButton = new JButton("+");
        subButton = new JButton("-");
        mulButton = new JButton("*");
        divButton = new JButton("/");
        decButton = new JButton(".");
        equButton = new JButton("=");
        delButton = new JButton("del");
        clrButton = new JButton("AC");
        negButton = new JButton("(-)");
        elbButton = new JButton("ELB");
        teeButton = new JButton("TEE");
        redButton = new JButton("RED");
        othButton = new JButton("ETC");

        functionButtons[0] = addButton;
        functionButtons[1] = subButton;
        functionButtons[2] = mulButton;
        functionButtons[3] = divButton;
        functionButtons[4] = equButton;
        functionButtons[5] = decButton;
        functionButtons[6] = delButton;
        functionButtons[7] = clrButton;
        functionButtons[8] = negButton;
        functionButtons[9] = delButton;
        functionButtons[10] = elbButton;
        functionButtons[11] = teeButton;
        functionButtons[12] = redButton;
        functionButtons[13] = othButton;

//각 객체마다 addActionListener 할당
        for(int i=0; i< 9; i++){
            functionButtons[i].addActionListener(this);
            functionButtons[i].setFont(baseFont);
            functionButtons[i].setFocusable(false);
        }
        for(int i=10; i<13; i++){
            functionButtons[i].addActionListener(this);
            functionButtons[i].setFont(fittingFont);
            functionButtons[i].setFocusable(false);
        }

//-------------------0-9까지의 숫자 버튼 생성--------------//
        for(int i=0; i<10; i++){
            numberButtons[i] = new JButton(String.valueOf(i));
            numberButtons[i].addActionListener(this);
            numberButtons[i].setFont(baseFont);
            numberButtons[i].setFocusable(false);
        }

        negButton.setBounds(50,580,100,50);
        delButton.setBounds(150,580,100,50);
        clrButton.setBounds(250,580,100,50);

        panel = new JPanel();
        panel.setBounds(50,150,300,400);
        panel.setLayout(new GridLayout(5,4, 10,10));

        panel.add(numberButtons[1]);
        panel.add(numberButtons[2]);
        panel.add(numberButtons[3]);
        panel.add(addButton);
        panel.add(numberButtons[4]);
        panel.add(numberButtons[5]);
        panel.add(numberButtons[6]);
        panel.add(subButton);
        panel.add(numberButtons[7]);
        panel.add(numberButtons[8]);
        panel.add(numberButtons[9]);
        panel.add(mulButton);
        panel.add(decButton);
        panel.add(numberButtons[0]);
        panel.add(equButton);
        panel.add(divButton);
        panel.add(elbButton);
        panel.add(teeButton);
        panel.add(redButton);
        panel.add(othButton);

//        panel.setBackground(Color.GRAY);

        frame.add(panel);
        frame.add(negButton);
        frame.add(delButton);
        frame.add(clrButton);
        frame.add(textArea);
        frame.setVisible(true);
    }

    public static void main(String[] args) {
        new CalculatorPiping();
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        for (int i = 0; i < 10; i++) {
            if (e.getSource() == numberButtons[i]) {
                if (startNewNo) {
                    textArea.setText("");
                    startNewNo = false;
                }
                textArea.setText(textArea.getText().concat(String.valueOf(i)));
            }
        }

        if (e.getSource() == elbButton) {
            textArea.setText("Elbow: ");
            startNewNo = false;
        }
        if (e.getSource() == teeButton) {
            textArea.setText(("Tee: "));
            startNewNo = false;
        }
        if (e.getSource() == redButton){
            textArea.setText("Reducer: ");
            startNewNo =false;
        }
        if (e.getSource() == decButton) {
            textArea.setText(textArea.getText().concat("."));
        }
        if (e.getSource() == addButton) {
            startNewNo = true;
            num1 = Double.parseDouble(textArea.getText());
            operator = '+';
        }
        if (e.getSource() == subButton) {
            startNewNo = true;
            num1 = Double.parseDouble(textArea.getText());
            operator = '-';
        }
        if (e.getSource() == mulButton) {
            if (textArea.getText().contains("Tee: ") | textArea.getText().contains("Reducer: ")) {
                if (textArea.getText().contains("*")) {
                    startNewNo = true;
                    operator = '*';
                }
                else {
                    String nowText = textArea.getText();
                    textArea.setText(nowText + " * ");
                }
            }
            else {
                num1 = Double.parseDouble(textArea.getText());
                startNewNo = true;
                operator = '*';
            }
        }
        if (e.getSource() == divButton) {
            startNewNo = true;
            num1 = Double.parseDouble(textArea.getText());
            operator = '/';
        }
        if (e.getSource() == equButton) {
            num2 = Double.parseDouble(textArea.getText());

            switch (operator) {
                case '+':
                    result = num1 + num2;
                    break;
                case '-':
                    result = num1 - num2;
                    break;
                case '*':
                    result = num1 * num2;
                    break;
                case '/':
                    result = num1 / num2;
                    break;
            }
            textArea.setText(String.valueOf(result));
            startNewNo = true;
        }
        if (e.getSource() == clrButton) {
            textArea.setText("");
        }
        if (e.getSource() == delButton) {
            String string = textArea.getText();
            textArea.setText("");
            for (int i = 0; i < string.length() - 1; i++) {
                textArea.setText(textArea.getText() + string.charAt(i));
            }
        }
        if (e.getSource() == negButton) {
            double temp = Double.parseDouble(textArea.getText());
            temp *= -1;
            textArea.setText(String.valueOf(temp));
        }
    }
}
