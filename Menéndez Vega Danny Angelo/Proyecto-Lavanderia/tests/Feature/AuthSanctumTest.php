<?php

namespace Tests\Feature;

use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Foundation\Testing\WithFaker;
use Tests\TestCase;


class AuthSanctumTest extends TestCase
{
    use RefreshDatabase;
    /** @test */
    public function authenticated_user_can_access_protected_route()
    {
        $user = User::factory()->create();
        $response = $this->actingAs($user, 'sanctum')->get('/api/user');
        $response->assertStatus(200);
    }

    /** @test */
    public function unauthenticated_user_cannot_access_protected_route()
    {
        $response = $this->getJson('/api/user');
        $response->assertStatus(401);
    }
}

