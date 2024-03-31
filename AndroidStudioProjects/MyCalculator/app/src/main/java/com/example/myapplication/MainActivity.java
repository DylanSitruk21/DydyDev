package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    public static int equation = 0;
    public static int result = 0;
    public static int lastBtn = 0;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button addBtn = (Button)findViewById(R.id.addBtn);
        addBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                EditText numEditText = (EditText) findViewById(R.id.Equation);
                TextView resultTextView = (TextView) findViewById(R.id.Result);
                equation = Integer.parseInt(numEditText.getText().toString());

                switch (lastBtn){
                    case 0:
                    case 1:
                        result = result + equation;break;
                    case 2: result = result - equation;break;
                    case 3: result = result * equation;break;
                    case 4: result = result / equation;break;
                    default: break;
                }

                resultTextView.setText(result+"");
                numEditText.setText("");
                lastBtn = 1;
            }
        });

        Button subBtn = (Button)findViewById(R.id.subBtn);
        subBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                EditText numEditText = (EditText) findViewById(R.id.Equation);
                TextView resultTextView = (TextView) findViewById(R.id.Result);
                equation = Integer.parseInt(numEditText.getText().toString());

                switch (lastBtn){
                    case 0:
                    case 1:
                        result = result + equation;break;
                    case 2: result = result - equation;break;
                    case 3: result = result * equation;break;
                    case 4: result = result / equation;break;
                    default: break;
                }

                resultTextView.setText(result+"");
                numEditText.setText("");
                lastBtn=2;
            }
        });

        Button multBtn = (Button)findViewById(R.id.multBtn);
        multBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                EditText numEditText = (EditText) findViewById(R.id.Equation);
                TextView resultTextView = (TextView) findViewById(R.id.Result);
                equation = Integer.parseInt(numEditText.getText().toString());

                switch (lastBtn){
                    case 0:
                    case 1:
                        result = result + equation;break;
                    case 2: result = result - equation;break;
                    case 3: result = result * equation;break;
                    case 4: result = result / equation;break;
                    default: break;
                }

                resultTextView.setText(result+"");
                numEditText.setText("");
                lastBtn=3;
            }
        });

        Button divBtn = (Button)findViewById(R.id.divBtn);
        divBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                EditText numEditText = (EditText) findViewById(R.id.Equation);
                TextView resultTextView = (TextView) findViewById(R.id.Result);
                equation = Integer.parseInt(numEditText.getText().toString());

                switch (lastBtn){
                    case 0:
                    case 1:
                        result = result + equation;break;
                    case 2: result = result - equation;break;
                    case 3: result = result * equation;break;
                    case 4: result = result / equation;break;
                    default: break;
                }

                resultTextView.setText(result+"");
                numEditText.setText("");
                lastBtn=4;
            }
        });

        final Button equalBtn = (Button)findViewById(R.id.equalBtn);
        equalBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                EditText numEditText = (EditText) findViewById(R.id.Equation);
                TextView resultTextView = (TextView) findViewById(R.id.Result);
                equation = Integer.parseInt(numEditText.getText().toString());
                switch (lastBtn){
                    case 0:
                    case 1:
                        result = result + equation;break;
                    case 2: result = result - equation;break;
                    case 3: result = result * equation;break;
                    case 4: result = result / equation;break;
                    case 5: result = equation;
                    default: break;
                }

                resultTextView.setText(result+"");
                numEditText.setText("");
                lastBtn = 5;
            }
        });

        Button resetBtn = (Button)findViewById(R.id.resetBtn);
        resetBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                EditText numEditText = (EditText) findViewById(R.id.Equation);
                TextView resultTextView = (TextView) findViewById(R.id.Result);
                result = 0;
                lastBtn = 0;
                resultTextView.setText(result+"");
                numEditText.setText("");
            }
        });
    }
}