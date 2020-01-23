package com.org.transport;
import java.awt.Button;
import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;


import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
import java.awt.Component;
import javax.swing.Box;


//主窗口：包含红绿灯参数的设置，以及南北路口和东西路口产生车的频率
public class SettingGui extends JFrame {
    static JTextField redText;
    static JTextField greenText;
    static JTextField delayText;
    static JTextField SNText;
    static JTextField EWText;


    public SettingGui() {
        getContentPane().setLayout(null);

        redText = new JTextField();
        redText.setBounds(351, 87, 86, 21);
        getContentPane().add(redText);
        redText.setColumns(10);

        //设置开始按钮，当点击开始按钮时，根据设置的参数画出交通图
        JButton startButton = new JButton("Start");
        startButton.setBounds(265, 332, 91, 23);
        getContentPane().add(startButton);

        greenText = new JTextField();
        greenText.setBounds(351, 136, 86, 21);
        getContentPane().add(greenText);
        greenText.setColumns(10);

        JLabel redLabel = new JLabel("Red light duration");
        redLabel.setBounds(73, 90, 243, 15);
        getContentPane().add(redLabel);

        JLabel greenLabel = new JLabel("Green light duration");
        greenLabel.setBounds(73, 139, 243, 15);
        getContentPane().add(greenLabel);

        Component verticalGlue = Box.createVerticalGlue();
        verticalGlue.setBounds(62, 87, 1, 1);
        getContentPane().add(verticalGlue);

        delayText = new JTextField();
        delayText.setBounds(351, 181, 86, 21);
        getContentPane().add(delayText);
        delayText.setColumns(10);

        JLabel delayLabel = new JLabel("Green light delay time");
        delayLabel.setBounds(73, 184, 227, 15);
        getContentPane().add(delayLabel);

        JLabel lblNewLabel = new JLabel("Vehicle gap at north-south inter.");
        lblNewLabel.setBounds(73, 235, 229, 15);
        getContentPane().add(lblNewLabel);

        SNText = new JTextField();
        SNText.setBounds(351, 232, 86, 21);
        getContentPane().add(SNText);
        SNText.setColumns(10);

        JLabel lblNewLabel_1 = new JLabel("Vehicle gap at east-west intersection");
        lblNewLabel_1.setBounds(73, 282, 234, 15);
        getContentPane().add(lblNewLabel_1);

        EWText = new JTextField();
        EWText.setBounds(351, 279, 86, 21);
        getContentPane().add(EWText);
        EWText.setColumns(10);

        JLabel label = new JLabel("Traffic system");
        label.setFont(new Font("宋体", Font.BOLD, 16));
        label.setBounds(228, 33, 149, 15);
        getContentPane().add(label);


        this.setSize(531, 443);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setVisible(true);

        SimpleListener ourListener = new SimpleListener();
        startButton.addActionListener(ourListener);
    }

    //监听开始按钮，当点击开始按钮时，新建画图窗口的FrameDemo类
    private class SimpleListener implements ActionListener {

        @Override
        public void actionPerformed(ActionEvent arg0) {
            // TODO Auto-generated method stub

            FrameDemo demo = new FrameDemo();
        }

    }

    public static void main(String[] args) {
        SettingGui demo = new SettingGui();
    }
}