<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class AuthController extends Controller
{
    public function login(Request $request)
    {
        $request->validate([
            'email' => 'required|email',
            'password' => 'required'
        ],['email.required'=>'Se requiere el email para autenticar','email.email'=>'El dato enviado no es un email','password.required'=>'La contraseña es requerida']);

        if (!auth()->attempt($request->only('email', 'password'))) {
            return response([
                'message' => 'Credenciales Invalidas'
            ], 401);
        }

        $user = auth()->user();

        $token = $user->createToken('token')->plainTextToken;

        return response([
            'user' => $user,
            'token' => $token
        ]);
    }

    public function logout()
    {
        auth()->user()->tokens()->delete();
        return response([
            'message' => 'Se ha cerrado la sesión.'
        ]);
    }


}
