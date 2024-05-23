<?php

namespace Tests\Feature;

use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Foundation\Testing\WithFaker;
use Tests\TestCase;

class GuestSanctumTest extends TestCase{
    use RefreshDatabase;
    public function test_authenticated_can_not_login()
{
    $user = User::factory()->create();

    // Autenticar al usuario
    $this->actingAs($user, 'sanctum');

    // Intentar iniciar sesión nuevamente
    $response = $this->postJson('/api/login', [
        'email' => $user->email,
        'password' => 'password', // Usar una contraseña válida pero no se debe permitir iniciar sesión ya que ya está autenticado
    ]);

    // Debería devolver un estado 403 (Forbiden)
    $response->assertStatus(403);
}
}
