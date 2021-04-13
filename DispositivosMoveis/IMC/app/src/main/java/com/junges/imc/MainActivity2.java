package com.junges.imc;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity2 extends AppCompatActivity {

    TextView rslNome;
    TextView rslPeso;
    TextView rslAltura;
    TextView imc;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);

        rslNome = findViewById(R.id.rslNome);
        rslPeso = findViewById(R.id.rslPeso);
        rslAltura = findViewById(R.id.rslAltura);
        imc = findViewById(R.id.imc);

        Bundle bundle = getIntent().getExtras();
        String nome = bundle.getString("nome");
        double peso = bundle.getDouble("peso");
        double altura = bundle.getDouble("altura");
        double imcCalc = peso / (altura * altura);
        rslNome.setText(nome);
        rslAltura.setText(String.valueOf(altura));
        rslPeso.setText(String.valueOf(peso));
        imc.setText(String.format("%.2f", imcCalc));
    }
}