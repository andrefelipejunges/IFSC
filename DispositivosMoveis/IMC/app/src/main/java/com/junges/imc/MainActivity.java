package com.junges.imc;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {

    EditText edtName;
    EditText edtPeso;
    EditText edtAltura3;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        edtName = findViewById(R.id.edtName);
        edtPeso = findViewById(R.id.edtPeso);
        edtAltura3 = findViewById(R.id.edtAltura3);
    }
    public void iniciaNovaActivity(View v){
        Intent i = new Intent(this, MainActivity2.class);
        String nome = edtName.getText().toString();
        double peso = Double.parseDouble(edtPeso.getText().toString());
        double altura = Double.parseDouble(edtAltura3.getText().toString());
        i.putExtra("nome", nome);
        i.putExtra("peso", peso);
        i.putExtra("altura", altura);
        startActivity(i);
    }
}